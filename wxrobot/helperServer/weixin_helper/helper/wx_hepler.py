# -*- coding: utf-8 -*-

import random, os, time, http.cookiejar, http.client, json, logging, re, sys, qrcode, subprocess
import urllib.request, urllib.parse, urllib.error, datetime, xml.dom.minidom
import urllib.request, urllib.error, urllib.parse, ssl
from urllib.parse import urlparse

import requests, platform, uuid
from pyqrcode import QRCode
from socket import timeout as timeout_error
from collections import defaultdict
from lxml import html

# for media upload
import mimetypes
from requests_toolbelt.multipart.encoder import MultipartEncoder
from twisted.internet.task import LoopingCall
from twisted.internet import endpoints, reactor

from common.common_setting import LOGIN_QRCODE_ROOT_PATH, helper_dict
from common.db_model.community_db.community_db_base import community_session_scope
from common.db_model.community_db.customer_info import CustomerInfo
from common.db_model.user_db.auth_db_base import user_session_scope
from common.db_model.user_db.helper_info import HelperInfo
from common.db_model.user_db.helper_users import HelperUsers
from common.thrift.body.ttypes import HelperLoginResp, LoginSuccessResp, ReceiveMessageResp, AddFriendQRResp
from common.thrift.define.ttypes import AppId, FunctionId, DirectionType, ResponseCode, MsgType
from common.thrift.head.ttypes import WxHead
from common.utils.logger import smart_log, start_twisted_logging

from multiprocessing import cpu_count
import threading
import multiprocessing

__author__ = 'jerry'

WX_HELPER_PROTO = None


def send_message(head, body):
    print("发送消息： head={}, body={}".format(head, body))
    global WX_HELPER_PROTO
    WX_HELPER_PROTO.send_msg(head=head, body=body, call_from_thread=True)


class HelperBasic(object):
    def __init__(self):
        pass


class WxHelper(HelperBasic):
    """
    一个管家对象
    """
    web_server_token = None  # 指定web server
    login_status = 0  # 登陆状态: 0:原始状态; 1:登录成功状态; 2:登录失败状态

    # TODO: 1、登出/掉线处理  2:加好友二维码; 3：**加群后将群设置为保存至通讯录
    def __init__(self, dict_=None, mark=None, web_server_token=None):
        self.web_server_token = web_server_token
        self.mark = mark
        self.DEBUG = False if not dict_ else dict_["DEBUG"]
        self.is_live = True if not dict_ else dict_["is_live"]
        self.uuid = '' if not dict_ else dict_["uuid"]
        self.base_uri = '' if not dict_ else dict_["base_uri"]
        self.redirect_uri = '' if not dict_ else dict_["redirect_uri"]
        self.uin = '' if not dict_ else dict_["uin"]
        self.sid = '' if not dict_ else dict_["sid"]
        self.skey = '' if not dict_ else dict_["skey"]
        self.pass_ticket = '' if not dict_ else dict_["pass_ticket"]
        self.deviceId = 'e' + repr(random.random())[2:17] if not dict_ else dict_["deviceId"]
        self.BaseRequest = {} if not dict_ else dict_["BaseRequest"]
        self.synckey = '' if not dict_ else dict_["synckey"]
        self.SyncKey = [] if not dict_ else dict_["SyncKey"]

        self.syncHost = '' if not dict_ else dict_["syncHost"]
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'
        self.interactive = False if not dict_ else dict_["interactive"]
        self.saveFolder = os.path.join(os.getcwd(), 'saved') if not dict_ else dict_["saveFolder"]
        self.saveSubFolders = {'webwxgeticon': 'icons', 'webwxgetheadimg': 'headimgs', 'webwxgetmsgimg': 'msgimgs',
                               'webwxgetvideo': 'videos', 'webwxgetvoice': 'voices', '_showQRCodeImg': 'qrcodes'}
        self.appid = 'wx782c26e4c19acffb'
        self.lang = 'zh_CN'
        self.lastCheckTs = time.time() if not dict_ else dict_["lastCheckTs"]
        self.SpecialUsers = ['newsapp', 'fmessage', 'filehelper', 'weibo', 'qqmail', 'fmessage', 'tmessage', 'qmessage',
                             'qqsync', 'floatbottle', 'lbsapp', 'shakeapp', 'medianote', 'qqfriend', 'readerapp',
                             'blogapp', 'facebookapp', 'masssendapp', 'meishiapp', 'feedsapp',
                             'voip', 'blogappweixin', 'weixin', 'brandsessionholder', 'weixinreminder',
                             'wxid_novlwrv3lqwv11', 'gh_22b87fa7cb3c', 'officialaccounts', 'notification_messages',
                             'wxid_novlwrv3lqwv11', 'gh_22b87fa7cb3c', 'wxitil', 'userexperience_alarm',
                             'notification_messages']
        self.TimeOut = 20  # 同步最短时间间隔（单位：秒）
        self.media_count = -1 if not dict_ else dict_["media_count"]

        self.cookie = http.cookiejar.CookieJar() if not dict_ else dict_["cookie"]
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cookie))
        opener.addheaders = [('User-agent', self.user_agent)]
        urllib.request.install_opener(opener)

        # 数据存储
        self.User = {} if not dict_ else dict_["User"]          # 管家自己
        self.contact_list = [] if not dict_ else dict_["ContactList"]  # 直接联系人
        self.group_map = {} if not dict_ else dict_["group_map"]  # 管家关联的群, (fixme: 需要置顶)
        self.group_member_map = {} if not dict_ else dict_["group_member_map"]  # 群成员对象
        self.member_group_map = {} if not dict_ else dict_["member_group_map"]  # 群成员对象对应群UserName
        self.group_to_member_list = {} if not dict_ else dict_["group_to_member_list"]
        self.helper_user_id = None if not dict_ else dict_["helper_user_id"]  # 当前管家服务的用户Id
        self.group_asy_map = {} if not dict_ else dict_["group_asy_map"]  # 开通的群 群信息是否同步到数据库<group_id, bool>

        # self.public_users_list = [] if not dict_ else dict_["PublicUsersList"]    # 公众号／服务号(暂时未用)
        # self.special_users_list = [] if not dict_ else dict_["SpecialUsersList"]  # 特殊账号(暂时未用)

    def web_wx_get_icon(self, _id):
        url = self.base_uri + \
              '/webwxgeticon?username=%s&skey=%s' % (id, self.skey)
        data = self._get(url)
        if data == '':
            return ''
        fn = 'img_' + _id + '.jpg'
        return self._save_file(fn, data, 'webwxgeticon')

    def web_wx_get_head_img(self, id):
        url = self.base_uri + \
              '/webwxgetheadimg?username=%s&skey=%s' % (id, self.skey)
        data = self._get(url)
        if data == '':
            return ''
        fn = 'img_' + id + '.jpg'
        return self._save_file(fn, data, 'webwxgetheadimg')

    def get_group_name(self, _id):
        name = '未知群'
        if self.group_map.get(_id):
            name = self.group_map.get(_id)["NickName"]

        if name == '未知群':
            # 现有群里面查不到
            group_list = self.get_name_by_id(_id)
            for group in group_list:
                self.group_map.setdefault(group["UserName"], group)
                if group['UserName'] == _id:
                    name = group['NickName']
                    member_list = group['MemberList']
                    for member in member_list:
                        self.group_member_map[member["UserName"]] = member
                        g_list = self.member_group_map.get(member["UserName"])
                        if not g_list:
                            g_list = []
                        g_list.append(group['UserName'])
                        self.member_group_map[member["UserName"]] = g_list

        return name

    def _show_qrcode_img(self, _str):
        url = 'https://login.weixin.qq.com/qrcode/' + self.uuid
        params = {
            't': 'webwx',
            '_': int(time.time())
        }

        data = self._post(url, params, False)
        if data == '':
            return

        if not os.path.exists(LOGIN_QRCODE_ROOT_PATH):
            os.makedirs(LOGIN_QRCODE_ROOT_PATH)

        qr_code_path = os.path.join(LOGIN_QRCODE_ROOT_PATH, str(datetime.datetime.now().year),
                                    str(datetime.datetime.now().month), str(datetime.datetime.now().day))

        if not os.path.exists(qr_code_path):
            os.makedirs(qr_code_path)

        file_path = os.path.join(qr_code_path, str(uuid.uuid4()) + '.jpg')
        with open(file_path, 'wb') as f:
            f.write(data)
            f.close()
        smart_log("登陆二维码地址: {}".format(file_path))

        head_ = WxHead()
        head_.helperToken = self.uin
        head_.appId = AppId.AppType_WebServer
        head_.functionId = FunctionId.HelperServer_HelperLogin
        head_.direction = DirectionType.ToWebServer
        # 返回指定的web 服务
        head_.tag = 2
        head_.mark = self.mark
        head_.serverTokenId = self.web_server_token
        resp = HelperLoginResp()
        resp.qrCodeUrl = file_path.split("web")[1]
        send_message(head_, resp)

    def wait_for_login(self, tip=0):
        time.sleep(tip)
        url = 'https://login.weixin.qq.com/cgi-bin/mmwebwx-bin/login?tip=%s&uuid=%s&_=%s' % (
            tip, self.uuid, int(time.time()))
        data = self._get(url)
        if data == '':
            return False
        pm = re.search(r"window.code=(\d+);", data)
        code = pm.group(1)

        if code == '201':
            return True
        elif code == '200':
            pm = re.search(r'window.redirect_uri="(\S+?)";', data)
            r_uri = pm.group(1) + '&fun=new'
            self.redirect_uri = r_uri
            self.base_uri = r_uri[:r_uri.rfind('/')]
            return True
        elif code == '408':
            print("[登陆超时] ")
        else:
            print("[登陆异常] ")
        return False

    def web_wx_init(self):
        """
        微信初始化, 内容存在微信群信息
        :return:
        """
        url = self.base_uri + '/webwxinit?pass_ticket=%s&skey=%s&r=%s' % (
            self.pass_ticket, self.skey, int(time.time()))
        params = {
            'BaseRequest': self.BaseRequest
        }
        dic = self._post(url, params)
        if dic == '':
            return False
        self.SyncKey = dic['SyncKey']
        self.User = dic['User']
        # synckey for synccheck
        self.synckey = '|'.join(
            [str(keyVal['Key']) + '_' + str(keyVal['Val']) for keyVal in self.SyncKey['List']])

        # 群信息(不处理群信息)
        # contact_list = dic["ContactList"]
        # for item in contact_list:
        #     if item['UserName'] and str(item['UserName']).startswith("@@"):
        #         self.group_map[item['UserName']] = item
        #         if item.get("MemberList"):
        #             self.group_to_member_list[item['UserName']] = item.get("MemberList")
        #         # 群成员
        #         if item["MemberList"] and len(item["MemberList"]) > 0:
        #             for member in item["MemberList"]:
        #                 self.group_member_map[member["UserName"]] = member
        #                 g_list = self.member_group_map.get(member["UserName"])
        #                 if not g_list:
        #                     g_list = []
        #                 g_list.append(item['UserName'])
        #                 self.member_group_map[member["UserName"]] = g_list

        # 保存信息到 redis
        global WX_HELPER_PROTO
        from common.redis.helper_session import HelperSession
        helper_session = HelperSession(helper_token=self.uin,
                                       helper_server_token=WX_HELPER_PROTO.get_server_token_id())
        helper_session.save_helper()

        # 保存助手信息
        with user_session_scope() as session:
            code, helper = HelperInfo.create_helper(session=session, helper_uin=self.uin,
                                                    nick_name=self.User.get("NickName"))
            code, helper_user = HelperUsers.get_helper_user_by_local_helper_uin(session=session, helper_uin=self.uin)
        if code == ResponseCode.Succeed and helper_user:
            self.helper_user_id = helper_user.UserId

        # 发送消息
        head_ = WxHead()
        head_.helperToken = self.uin
        head_.appId = AppId.AppType_WebServer
        head_.functionId = FunctionId.HelperServer_LoginSuccess
        head_.direction = DirectionType.ToWebServer
        # 返回指定的web 服务
        head_.tag = 2
        head_.serverTokenId = self.web_server_token
        head_.mark = self.mark
        resp = LoginSuccessResp()
        resp.wxuin = self.uin
        send_message(head_, resp)

        return dic['BaseResponse']['Ret'] == 0

    def web_wx_status_notify(self):
        """
        状态通知
        :return:
        """
        url = self.base_uri + \
              '/webwxstatusnotify?lang=zh_CN&pass_ticket=%s' % (self.pass_ticket)
        params = {
            'BaseRequest': self.BaseRequest,
            "Code": 3,
            "FromUserName": self.User['UserName'],
            "ToUserName": self.User['UserName'],
            "ClientMsgId": int(time.time())
        }
        dic = self._post(url, params)
        if dic == '':
            return False

        return dic['BaseResponse']['Ret'] == 0

    def web_wx_get_contact(self):
        """
        获取联系人,
        :return:
        """
        # FIXME 触发一定条件, 执行更新
        SpecialUsers = self.SpecialUsers
        url = self.base_uri + '/webwxgetcontact?pass_ticket=%s&skey=%s&r=%s' % (
            self.pass_ticket, self.skey, int(time.time()))
        dic = self._post(url, {})
        if dic == '':
            return False

        contact_list = dic['MemberList']

        for i in range(len(contact_list) - 1, -1, -1):
            contact = contact_list[i]
            if contact['VerifyFlag'] & 8 != 0:  # 公众号/服务号
                contact_list.remove(contact)
                # self.public_users_list.append(Contact)
            elif contact['UserName'] in SpecialUsers:  # 特殊账号
                contact_list.remove(contact)
                # self.special_users_list.append(contact)
            elif contact['UserName'] and str(contact['UserName']).startswith("@@"):  # 群聊
                contact_list.remove(contact)
                self.group_map[contact['UserName']] = contact
                if contact.get("MemberList"):
                    self.group_to_member_list[contact['UserName']] = contact.get("MemberList")
                # 群成员
                if contact["MemberList"] and len(contact["MemberList"]) > 0:
                    for member in contact["MemberList"]:
                        self.group_member_map[member["UserName"]] = member
                        g_list = self.member_group_map.get(member["UserName"])
                        if not g_list:
                            g_list = []
                        g_list.append(contact['UserName'])
                        self.member_group_map[member["UserName"]] = g_list
            elif contact['UserName'] == self.User['UserName']:  # 自己
                contact_list.remove(contact)
                # elif Contact["UserName"] and str(Contact["UserName"]).startswith("@"):  # 排除群聊后的联系人
                #     # 标记
                #     is_exist = False
                #     if Contact['RemarkName'] and len(str(Contact['RemarkName']).split(",")) > 1:
                #         s_list = str(Contact['RemarkName']).split(",")
                #         try:
                #             temp_id = s_list[len(s_list) - 1]
                #             with user_session_scope() as session:
                #                 code, record = HelperUsers.get_helper_user_by_local_helper_uin(session=session,
                #                                                                                helper_uin=str(self.uin))
                #             if code == ResponseCode.Succeed and record:
                #                 is_exist = True
                #         except Exception as e:
                #             logging.exception(e)

        self.contact_list = contact_list

        return True

    def web_wx_batch_get_contact(self, group_name_list=None):
        """
        批量获取群联系人
        :return:
        """
        url = self.base_uri + \
              '/webwxbatchgetcontact?type=ex&r=%s&pass_ticket=%s' % (
                  int(time.time()), self.pass_ticket)
        params = {
            'BaseRequest': self.BaseRequest,
            "Count": len(self.group_map) if not group_name_list else len(group_name_list),
            "List": [{"UserName": g['UserName'], "EncryChatRoomId": ""} for user_name, g in self.group_map.items()]
            if not group_name_list else [{"UserName": g, "EncryChatRoomId": ""} for g in group_name_list]
        }
        dic = self._post(url, params)
        if dic == '':
            return False

        contact_list = dic['ContactList']
        # ContactCount = dic['Count']

        for i in range(len(contact_list) - 1, -1, -1):
            contact = contact_list[i]
            if not self.group_map.get(contact["UserName"]):
                self.group_map[contact["UserName"]] = contact
            member_list = contact['MemberList']
            if member_list and len(member_list) > 0:
                self.group_to_member_list[contact['UserName']] = member_list
            for member in member_list:
                self.group_member_map[member["UserName"]] = member
                g_list = self.member_group_map.get(member["UserName"])
                if not g_list:
                    g_list = []
                g_list.append(contact['UserName'])
                self.member_group_map[member["UserName"]] = g_list

        return True

    def get_name_by_id(self, _id):
        """

        :param _id:
        :return:
        """
        # TODO
        url = self.base_uri + \
              '/webwxbatchgetcontact?type=ex&r=%s&pass_ticket=%s' % (
                  int(time.time()), self.pass_ticket)
        params = {
            'BaseRequest': self.BaseRequest,
            "Count": 1,
            "List": [{"UserName": _id, "EncryChatRoomId": ""}]
        }
        dic = self._post(url, params)
        if dic == '':
            return None

        return dic['ContactList']

    def listen_msg_mode(self):
        """
        监听消息
        :return:
        """
        smart_log('[*] 进入消息监听模式 ... 成功')
        self._run('[*] 进行同步线路测试 ... ', self.test_sync_check)
        play_we_chat = 0
        red_envelope = 0
        while self.is_live:
            self.lastCheckTs = time.time()
            [retcode, selector] = self.sync_check()
            if self.DEBUG:
                print('retcode: %s, selector: %s' % (retcode, selector))
            smart_log('retcode: %s, selector: %s' % (retcode, selector))
            if retcode == '1100':
                smart_log('[*] 在手机或者未知情况登出助手!')
                with user_session_scope() as session:
                    r_ = HelperInfo.update_status_by_uin(session=session, helper_uin=self.uin, status=2)
                break
            if retcode == '1101':
                smart_log('[*] 你在手机上登出了微信或者你在其他地方登录了 WEB 版微信!')
                with user_session_scope() as session:
                    r_ = HelperInfo.update_status_by_uin(session=session, helper_uin=self.uin, status=2)
                # TODO 发送通知消息
                break
            elif retcode == '0':
                if selector == '2':  # 2: 文本消息/表情/图片/语言/位置/红包/名片/收藏/文件/外部分享/修改群名称/群公告修改/新群员加入
                    r = self.web_wx_sync()
                    if r is not None:
                        self.handle_msg(r)
                elif selector == '4':
                    r = self.web_wx_sync()
                    if r is not None:
                        self.handle_msg(r)

                elif selector == '6':
                    # FIXME 未发现该类型消息
                    smart_log('[*] retcode={}， selector={} 未知消息类型'.format(retcode, selector))
                    r = self.web_wx_sync()
                    if r is not None:
                        self.handle_msg(r)

                elif selector == '7':
                    play_we_chat += 1
                    smart_log('[*] 你在手机上玩微信被我发现了 %d 次' % play_we_chat)
                    r = self.web_wx_sync()
                elif selector == '0':
                    time.sleep(1)
            if (time.time() - self.lastCheckTs) <= 20:
                time.sleep(time.time() - self.lastCheckTs)

    def test_sync_check(self):
        """
        同步线路测试
        :return:
        """
        SyncHost = ['wx2.qq.com',
                    'webpush.wx2.qq.com',
                    'wx8.qq.com',
                    'webpush.wx8.qq.com',
                    'qq.com',
                    'webpush.wx.qq.com',
                    'web2.wechat.com',
                    'webpush.web2.wechat.com',
                    'wechat.com',
                    'webpush.web.wechat.com',
                    'webpush.weixin.qq.com',
                    'webpush.wechat.com',
                    'webpush1.wechat.com',
                    'webpush2.wechat.com',
                    'webpush.wx.qq.com',
                    'webpush2.wx.qq.com']
        for host in SyncHost:
            self.syncHost = host
            [retcode, selector] = self.sync_check()
            if retcode == '0':
                return True
        return False

    def sync_check(self):
        """
        同步线路检查
        https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxsync
        :return:
        """
        params = {
            'r': int(time.time()),
            'sid': self.sid,
            'uin': self.uin,
            'skey': self.skey,
            'deviceid': self.deviceId,
            'synckey': self.synckey,
            '_': int(time.time()),
        }
        url = 'https://' + self.syncHost + '/cgi-bin/mmwebwx-bin/synccheck?' + urllib.parse.urlencode(params)
        data = self._get(url, timeout=30)
        if data == '':
            return [-1, -1]

        pm = re.search(
            r'window.synccheck={retcode:"(\d+)",selector:"(\d+)"}', data)
        retcode = pm.group(1)
        selector = pm.group(2)
        return [retcode, selector]

    def web_wx_sync(self):
        """
        同步线路
        :return:
        """
        url = self.base_uri + \
              '/webwxsync?sid=%s&skey=%s&pass_ticket=%s' % (
                  self.sid, self.skey, self.pass_ticket)
        params = {
            'BaseRequest': self.BaseRequest,
            'SyncKey': self.SyncKey,
            'rr': ~int(time.time())
        }
        dic = self._post(url, params)
        if dic == '':
            return None
        if self.DEBUG:
            print(json.dumps(dic, indent=4))
            (json.dumps(dic, indent=4))

        if dic['BaseResponse']['Ret'] == 0:
            self.SyncKey = dic['SyncKey']
            self.synckey = '|'.join(
                [str(keyVal['Key']) + '_' + str(keyVal['Val']) for keyVal in self.SyncKey['List']])

        # top_contact_list = dic["ModContactList"]
        # # print("最近修改的 List = {}".format(top_contact_list))
        # if top_contact_list and len(top_contact_list) > 0:
        #     for top_item in top_contact_list:
        #         self.group_map[top_item["UserName"]] = top_item
        #         # 群成员
        #         if top_item["MemberList"] and len(top_item["MemberList"]) > 0:
        #             for member in top_item["MemberList"]:
        #                 self.group_member_map[member["UserName"]] = member
        #                 self.member_group_map[member["UserName"]] = top_item['UserName']
        return dic

    def web_wx_send_msg(self, word, to='filehelper'):
        """
        发送消息?
        :param word:
        :param to:
        :return:
        """
        # TODO
        url = self.base_uri + '/webwxsendmsg?pass_ticket=%s' % (self.pass_ticket)
        client_msg_id = str(int(time.time() * 1000)) + \
                        str(random.random())[:5].replace('.', '')
        params = {
            'BaseRequest': self.BaseRequest,
            'Msg': {
                "Type": 1,
                "Content": self._trans_coding(word),
                "FromUserName": self.User['UserName'],
                "ToUserName": to,
                "LocalID": client_msg_id,
                "ClientMsgId": client_msg_id
            },
            "Scene": 0
        }
        headers = {'content-type': 'application/json; charset=UTF-8'}
        data = json.dumps(params, ensure_ascii=False).encode('utf8')
        r = requests.post(url, data=data, headers=headers)
        dic = r.json()
        return dic['BaseResponse']['Ret'] == 0

    def _trans_coding(self, data):
        if not data:
            return data
        result = None
        if type(data) == str:
            result = data
        elif type(data) == str:
            result = data.decode('utf-8')
        return result

    def web_wx_upload_media(self, image_name):
        """
        上传媒体文件?
        :param image_name:
        :return:
        """
        url = 'https://file2.wx.qq.com/cgi-bin/mmwebwx-bin/webwxuploadmedia?f=json'
        # 计数器
        self.media_count = self.media_count + 1
        # 文件名
        file_name = image_name
        # MIME格式
        # mime_type = application/pdf, image/jpeg, image/png, etc.
        mime_type = mimetypes.guess_type(image_name, strict=False)[0]
        # 微信识别的文档格式，微信服务器应该只支持两种类型的格式。pic和doc
        # pic格式，直接显示。doc格式则显示为文件。
        media_type = 'pic' if mime_type.split('/')[0] == 'image' else 'doc'
        # 上一次修改日期
        lastModifieDate = 'Thu Mar 17 2016 00:55:10 GMT+0800 (CST)'
        # 文件大小
        file_size = os.path.getsize(file_name)
        # PassTicket
        pass_ticket = self.pass_ticket
        # clientMediaId
        client_media_id = str(int(time.time() * 1000)) + \
                          str(random.random())[:5].replace('.', '')
        # webwx_data_ticket
        webwx_data_ticket = ''
        for item in self.cookie:
            if item.name == 'webwx_data_ticket':
                webwx_data_ticket = item.value
                break
        if (webwx_data_ticket == ''):
            return "None Fuck Cookie"

        uploadmediarequest = json.dumps({
            "BaseRequest": self.BaseRequest,
            "ClientMediaId": client_media_id,
            "TotalLen": file_size,
            "StartPos": 0,
            "DataLen": file_size,
            "MediaType": 4
        }, ensure_ascii=False).encode('utf8')

        multipart_encoder = MultipartEncoder(
            fields={
                'id': 'WU_FILE_' + str(self.media_count),
                'name': file_name,
                'type': mime_type,
                'lastModifieDate': lastModifieDate,
                'size': str(file_size),
                'mediatype': media_type,
                'uploadmediarequest': uploadmediarequest,
                'webwx_data_ticket': webwx_data_ticket,
                'pass_ticket': pass_ticket,
                'filename': (file_name, open(file_name, 'rb'), mime_type.split('/')[1])
            },
            boundary='-----------------------------1575017231431605357584454111'
        )

        headers = {
            'Host': 'file2.wx.qq.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:42.0) Gecko/20100101 Firefox/42.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'https://wx2.qq.com/',
            'Content-Type': multipart_encoder.content_type,
            'Origin': 'https://wx2.qq.com',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache'
        }

        r = requests.post(url, data=multipart_encoder, headers=headers)
        response_json = r.json()
        if response_json['BaseResponse']['Ret'] == 0:
            return response_json
        return None

    def send_img(self, username, file_name):
        """
        发送图片
        :param username:
        :param file_name:
        :return:
        """
        response = self.web_wx_upload_media(file_name)
        media_id = ""
        if response is not None:
            media_id = response['MediaId']
        response = self.web_wx_send_msg_img(username, media_id)

    def web_wx_send_msg_img(self, user_id, media_id):
        url = 'https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxsendmsgimg?fun=async&f=json&pass_ticket=%s' % self.pass_ticket
        client_msg_id = str(int(time.time() * 1000)) + \
                      str(random.random())[:5].replace('.', '')
        data_json = {
            "BaseRequest": self.BaseRequest,
            "Msg": {
                "Type": 3,
                "MediaId": media_id,
                "FromUserName": self.User['UserName'],
                "ToUserName": user_id,
                "LocalID": client_msg_id,
                "ClientMsgId": client_msg_id
            }
        }
        headers = {'content-type': 'application/json; charset=UTF-8'}
        data = json.dumps(data_json, ensure_ascii=False).encode('utf8')
        r = requests.post(url, data=data, headers=headers)
        dic = r.json()
        return dic['BaseResponse']['Ret'] == 0

    def send_emotion(self, username, file_name):
        """
        发送表情
        :param username:
        :param file_name:
        :return:
        """
        response = self.web_wx_upload_media(file_name)
        media_id = ""
        if response is not None:
            media_id = response['MediaId']
        response = self.web_wx_send_msg_emotion(username, media_id)

    def web_wx_send_msg_emotion(self, user_id, media_id):
        url = 'https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxsendemoticon?fun=sys&f=json&pass_ticket=%s' % self.pass_ticket
        clientMsgId = str(int(time.time() * 1000)) + \
                      str(random.random())[:5].replace('.', '')
        data_json = {
            "BaseRequest": self.BaseRequest,
            "Msg": {
                "Type": 47,
                "EmojiFlag": 2,
                "MediaId": media_id,
                "FromUserName": self.User['UserName'],
                "ToUserName": user_id,
                "LocalID": clientMsgId,
                "ClientMsgId": clientMsgId
            }
        }
        headers = {'content-type': 'application/json; charset=UTF-8'}
        data = json.dumps(data_json, ensure_ascii=False).encode('utf8')
        r = requests.post(url, data=data, headers=headers)
        dic = r.json()
        if self.DEBUG:
            print(json.dumps(dic, indent=4))
            logging.debug(json.dumps(dic, indent=4))
        return dic['BaseResponse']['Ret'] == 0

    def web_wx_verify_user(self, is_pass=True, v_user_name=None, v_ticket=None):
        """
        https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxverifyuser?r=1523163838452
        好友请求验证通过
        :return:
        """
        url = self.base_uri + '/webwxverifyuser?r=%s' % (int(time.time()))
        if is_pass:
            params = {
                'BaseRequest': self.BaseRequest,
                "Opcode": 3,
                "SceneList": [33],
                "SceneListCount": 1,
                "skey": self.skey,
                "VerifyContent": "",
                "VerifyUserList": [{"Value": v_user_name, "VerifyUserTicket": v_ticket}],
                "VerifyUserListSize": 1,
            }
            dic_ = self._post(url, params)
            if dic_ == '':
                return False
            print("验证成功!")
            return dic_['BaseResponse']['Ret'] == 0

    def check_group_is_buy(self, username):
        """
        检查群
        :param username:
        :return: isBuy, groupId, show_name, groupName
        """
        group_ = self.get_group_by_name(username)
        if not group_:
            return False, None, None, None
        # self.User['UserName']
        member_list = self.group_to_member_list.get(username)
        if not member_list:
            return False, None, None, None
        for member in member_list:
            if member["UserName"] == self.User["UserName"] and member["DisplayName"]:
                display_name = member["DisplayName"]
                _list = str(display_name).split("#")
                if len(_list) > 1:
                    return True, _list[len(_list) - 1], display_name, group_["NickName"]
                else:
                    return False, None, None, None
        return False, None, None, None

    def get_group_by_name(self, username):
        """

        :param username:
        :return:
        """
        group_ = self.group_map.get(username)
        if not group_:
            self.web_wx_batch_get_contact(group_name_list=[username])
            group_ = self.group_map.get(username)
        return group_

    def handle_msg(self, r):
        """
        处理接收到的消息
        :param r:
        :return:
        """
        for msg in r['AddMsgList']:
            print('[*] 你有新的消息，请注意查收')
            logging.debug('[*] 你有新的消息，请注意查收')
            # TODO 保存至 mongo

            if self.DEBUG:
                fn = 'msg' + str(int(random.random() * 1000)) + '.json'
                with open(fn, 'w') as f:
                    f.write(json.dumps(msg))
                print('[*] 该消息已储存到文件: ' + fn)
                logging.debug('[*] 该消息已储存到文件: %s' % (fn))

            msg_type = msg['MsgType']
            # form_name = self.get_user_remark_name(msg['FromUserName'])
            # content = msg['Content'].replace('&lt;', '<').replace('&gt;', '>')
            # content = msg['Content'][71:]
            content = ''.join(msg['Content'].split("<br/>")[1:])
            msgid = msg['MsgId']
            original_content = msg["Content"]

            # 判断群是否拉取到
            is_buy = 0
            group_id = 0
            show_name = None
            group_name = None
            if msg['FromUserName'] and str(msg['FromUserName']).startswith("@@"):
                buy_bool, g_id, show_name, g_name = self.check_group_is_buy(msg['FromUserName'])
                print("是否购买: {}, 群Id: {}, 展示名称: {}, 群名称: {}".format(buy_bool, g_id, show_name, g_name))
                if buy_bool and g_id:
                    is_buy = 1
                    group_id = g_id
                    group_name = g_name
                else:
                    # FIXME 发送消息通知开通
                    print("此群未开通，发送消息通知购买开通")
                    self.web_wx_batch_get_contact(group_name_list=[msg['FromUserName']])

            # 更新群信息到数据库
            if not self.group_asy_map.get(group_id) and group_id and group_id != 0:
                with user_session_scope() as session:
                    from common.db_model.user_db.group_info import GroupInfo
                    b_ = GroupInfo.update_asy_group_info(session=session, group_id=group_id,
                                                         user_name=msg['FromUserName'],
                                                         status=2, other_json=None, helper_show=show_name,
                                                         group_name=group_name,
                                                         user_id=self.helper_user_id if self.helper_user_id else None)
                if b_:
                    self.group_asy_map.setdefault(group_id, True)

            if msg_type == 1:  # 文本消息、表情、位置
                # raw_msg = {'raw_msg': msg}
                smart_log("msgType=1, msg={}".format(msg))
                form_user_name = msg["FromUserName"]
                to_user_name = msg["ToUserName"]
                msg_type = msg["MsgType"]
                auth = None
                if original_content:
                    auth = str(original_content)[0:65]
                rm_resp = ReceiveMessageResp()
                # 发送到 web_server , 识别是否为购买群
                rm_resp.isBuy = 2 if is_buy == 1 else 1
                rm_resp.formUserName = form_user_name
                rm_resp.toUserName = to_user_name
                rm_resp.msgType = 1
                rm_resp.author = auth
                rm_resp.content = content
                rm_resp.originalContent = original_content
                rm_resp.groupId = int(group_id)

                head_ = WxHead()
                head_.helperToken = self.uin
                head_.appId = AppId.AppType_WebServer
                head_.functionId = FunctionId.HelperServer_ReceiveMessage
                head_.direction = DirectionType.ToWebServer
                head_.mark = self.mark
                send_message(head_, rm_resp)

                # 关键词识别
                if is_buy and content and str(content).startswith("@{}".format(show_name)) and len(content) > len(
                        show_name) + 2:
                    with community_session_scope() as session:
                        from common.db_model.community_db.cust_keywords import CustKeywords
                        reply_content = CustKeywords.get_reply_by_keyword(session=session, group_id=group_id,
                                                                          keyword=str(content)[len(show_name) + 2:])
                    if reply_content:
                        self.web_wx_send_msg(reply_content, form_user_name)

            elif msg_type == 3:  # 图片
                pass
                # image = self.web_wx_get_msg_img(msgid)
                # raw_msg = {'raw_msg': msg,
                #            'message': '%s 发送了一张图片: %s' % (form_name, image)}
                # self._show_msg(raw_msg)
                # self._safe_open(image)
            elif msg_type == 34:  # 语言
                pass
                # voice = self.web_wx_get_voice(msgid)
                # raw_msg = {'raw_msg': msg,
                #            'message': '%s 发了一段语音: %s' % (form_name, voice)}
                # self._show_msg(raw_msg)
                # self._safe_open(voice)

            elif msg_type == 37:  # 请求添加好友, 自动校验
                print("请求添加好友， msg={}".format(msg))
                # if msg["RecommendInfo"] and msg["RecommendInfo"]["UserName"] and msg["RecommendInfo"]["Ticket"]:
                #     # 验证
                #     self.web_wx_verify_user(is_pass=True, v_user_name=msg["RecommendInfo"]["UserName"],
                #                             v_ticket=msg["RecommendInfo"]["Ticket"])
                #     # 取别名
                #     with user_session_scope() as session:
                #         code, user = HelperUsers.create_helper_user(session=session,
                #                                                     nick_name=msg["RecommendInfo"]["NickName"],
                #                                                     helper_uin=self.uin)
                #     if code == ResponseCode.Succeed:
                #         self.web_wx_op_log(type_=2, remark_name=msg["RecommendInfo"]["NickName"] + "," + user.UserId,
                #                            user_name=msg["RecommendInfo"]["UserName"])
                #     # 发送消息到 web_server , 有好友添加进来
                #     rm_resp = AddFriendQRResp()
                #     rm_resp.userId = user.UserId
                #     rm_resp.userName = msg["RecommendInfo"]["UserName"]
                #
                #     head_ = WxHead()
                #     head_.helperToken = self.uin
                #     head_.appId = AppId.AppType_WebServer
                #     head_.functionId = FunctionId.HelperServer_AddFriendQR
                #     head_.direction = DirectionType.ToWebServer
                #     head_.mark = self.mark
                #     send_message(head_, rm_resp)

            elif msg_type == 42:  # 名片
                info = msg['RecommendInfo']
                # print('%s 发送了一张名片:' % form_name)
                # print('=========================')
                # print('= 昵称: %s' % info['NickName'])
                # print('= 微信号: %s' % info['Alias'])
                # print('= 地区: %s %s' % (info['Province'], info['City']))
                # print('= 性别: %s' % ['未知', '男', '女'][info['Sex']])
                # print('=========================')
                # raw_msg = {'raw_msg': msg, 'message': '%s 发送了一张名片: %s' % (
                #     form_name.strip(), json.dumps(info))}
                # self._show_msg(raw_msg)
            elif msg_type == 43:  # 短视频
                pass
            elif msg_type == 47:
                pass
                # url = self._search_content('cdnurl', content)
                # raw_msg = {'raw_msg': msg,
                #            'message': '%s 发了一个动画表情，点击下面链接查看: %s' % (form_name, url)}
                # self._show_msg(raw_msg)
                # self._safe_open(url)
            elif msg_type == 49:  # 链接文章, 文件
                app_msg_type = defaultdict(lambda: "")
                app_msg_type.update({5: '链接', 3: '音乐', 7: '微博'})
                # print('%s 分享了一个%s:' % (form_name, app_msg_type[msg['AppMsgType']]))
                # print('=========================')
                # print('= 标题: %s' % msg['FileName'])
                # print('= 描述: %s' % self._search_content('des', content, 'xml'))
                # print('= 链接: %s' % msg['Url'])
                # print('= 来自: %s' % self._search_content('appname', content, 'xml'))
                # print('=========================')
                # card = {
                #     'title': msg['FileName'],
                #     'description': self._search_content('des', content, 'xml'),
                #     'url': msg['Url'],
                #     'appname': self._search_content('appname', content, 'xml')
                # }
                # raw_msg = {'raw_msg': msg, 'message': '%s 分享了一个%s: %s' % (
                #     form_name, app_msg_type[msg['AppMsgType']], json.dumps(card))}
                # self._show_msg(raw_msg)
            elif msg_type == 51:  # 助手用户点开群
                pass
                # raw_msg = {'raw_msg': msg, 'message': '[*] 成功获取联系人信息'}
                # self._show_msg(raw_msg)
            elif msg_type == 62:
                pass
                # video = self.web_wx_get_video(msgid)
                # raw_msg = {'raw_msg': msg,
                #            'message': '%s 发了一段小视频: %s' % (form_name, video)}
                # self._show_msg(raw_msg)
                # self._safe_open(video)
            elif msg_type == 10000:  # 你已添加了
                if str(original_content).startswith("你已添加了") \
                        or str(original_content).startswith("我通过了你的朋友验证请求，现在我们可以开始聊天了"):  # 更新

                    contact_list = self.get_name_by_id(msg["FromUserName"])
                    if contact_list and len(contact_list) == 1:
                        con_info = contact_list[0]
                        # 取别名
                        with user_session_scope() as session:
                            code, user = HelperUsers.create_helper_user(session=session,
                                                                        nick_name=con_info["NickName"],
                                                                        helper_uin=self.uin)
                            self.helper_user_id = user.UserId
                            bool_ = CustomerInfo.set_user_id_with_helper_uin(session=session, user_id=user.UserId,
                                                                             helper_uin=self.uin)

                        # if code == ResponseCode.Succeed:
                        #     self.web_wx_op_log(type_=2, remark_name=con_info["NickName"] + ",{}".format(user.UserId),
                        #                        user_name=con_info["UserName"])
                        # 发送消息到 web_server , 有好友添加进来
                        rm_resp = AddFriendQRResp()
                        rm_resp.userId = user.UserId
                        rm_resp.userName = con_info["UserName"]

                        head_ = WxHead()
                        head_.helperToken = self.uin
                        head_.appId = AppId.AppType_WebServer
                        head_.functionId = FunctionId.HelperServer_AddFriendQR
                        head_.direction = DirectionType.ToWebServer
                        head_.mark = self.mark
                        send_message(head_, rm_resp)

            elif msg_type == 10002:
                pass
                # raw_msg = {'raw_msg': msg, 'message': '%s 撤回了一条消息' % form_name}
                # self._show_msg(raw_msg)
            else:
                logging.debug('[*] 该消息类型为: %d，可能是表情，图片, 链接或红包: %s' %
                              (msg['MsgType'], json.dumps(msg)))
                # raw_msg = {
                #     'raw_msg': msg, 'message': '[*] 该消息类型为: %d，可能是表情，图片, 链接或红包' % msg['MsgType']}
                # self._show_msg(raw_msg)

    # Not work now for weixin haven't support this API
    def web_wx_get_video(self, msgid):
        url = self.base_uri + \
              '/webwxgetvideo?msgid=%s&skey=%s' % (msgid, self.skey)
        data = self._get(url, api='webwxgetvideo')
        if data == '':
            return ''
        fn = 'video_' + msgid + '.mp4'
        return self._save_file(fn, data, 'webwxgetvideo')

    def _search_content(self, key, content, fmat='attr'):
        if fmat == 'attr':
            pm = re.search(key + '\s?=\s?"([^"<]+)"', content)
            if pm:
                return pm.group(1)
        elif fmat == 'xml':
            pm = re.search('<{0}>([^<]+)</{0}>'.format(key), content)
            if not pm:
                pm = re.search(
                    '<{0}><\!\[CDATA\[(.*?)\]\]></{0}>'.format(key), content)
            if pm:
                return pm.group(1)
        return '未知'

    def web_wx_get_voice(self, msgid):
        url = self.base_uri + \
              '/webwxgetvoice?msgid=%s&skey=%s' % (msgid, self.skey)
        data = self._get(url, api='webwxgetvoice')
        if data == '':
            return ''
        fn = 'voice_' + msgid + '.mp3'
        return self._save_file(fn, data, 'webwxgetvoice')

    def web_wx_get_msg_img(self, msgid):
        url = self.base_uri + \
              '/webwxgetmsgimg?MsgID=%s&skey=%s' % (msgid, self.skey)
        data = self._get(url)
        if data == '':
            return ''
        fn = 'img_' + msgid + '.jpg'
        return self._save_file(fn, data, 'webwxgetmsgimg')

    def _save_file(self, filename, data, api=None):
        fn = filename
        if self.saveSubFolders[api]:
            dirName = os.path.join(self.saveFolder, self.saveSubFolders[api])
            if not os.path.exists(dirName):
                os.makedirs(dirName)
            fn = os.path.join(dirName, filename)
            logging.debug('Saved file: %s' % fn)
            with open(fn, 'wb') as f:
                f.write(data)
                f.close()
        return fn

    def _run(self, _str, func, *args):
        smart_log(_str)
        if func(*args):
            logging.debug('%s... 成功' % (_str))
        else:
            smart_log('%s... 失败' % (_str))

    def get_QRCode(self):
        """
        :return:
        """
        # return self._showQRCodeImg()
        if sys.platform.startswith('win'):
            self._show_qrcode_img('win')
        elif sys.platform.find('darwin') >= 0:
            self._show_qrcode_img('macos')
        elif sys.platform.startswith("linux"):
            self._show_qrcode_img("linux")
        else:
            self._str2qr('https://login.weixin.qq.com/l/' + self.uuid)

    def login(self):
        data = self._get(self.redirect_uri)
        if data == '':
            self.login_status = 2
            return False
        doc = xml.dom.minidom.parseString(data)
        root = doc.documentElement

        for node in root.childNodes:
            if node.nodeName == 'skey':
                self.skey = node.childNodes[0].data
            elif node.nodeName == 'wxsid':
                self.sid = node.childNodes[0].data
            elif node.nodeName == 'wxuin':
                self.uin = node.childNodes[0].data
            elif node.nodeName == 'pass_ticket':
                self.pass_ticket = node.childNodes[0].data

        if '' in (self.skey, self.sid, self.uin, self.pass_ticket):
            self.login_status = 2
            return False

        self.BaseRequest = {
            'Uin': int(self.uin),
            'Sid': self.sid,
            'Skey': self.skey,
            'DeviceID': self.deviceId,
        }
        self.login_status = 1

        helper_dict[self.uin] = self

        return True

    def get_uuid(self):
        url = 'https://login.weixin.qq.com/jslogin'
        params = {
            'appid': self.appid,
            'fun': 'new',
            'lang': self.lang,
            '_': int(time.time()),
        }
        # r = requests.get(url=url, params=params)
        # r.encoding = 'utf-8'
        # data = r.text
        data = self._post(url, params, False).decode("utf-8")
        if data == '':
            return False
        regx = r'window.QRLogin.code = (\d+); window.QRLogin.uuid = "(\S+?)"'
        pm = re.search(regx, data)
        if pm:
            code = pm.group(1)
            self.uuid = pm.group(2)
            return code == '200'
        return False

    def _get(self, url: object, api: object = None, timeout: object = None) -> object:
        request = urllib.request.Request(url=url)
        request.add_header('Referer', 'https://wx.qq.com/')
        if api == 'webwxgetvoice':
            request.add_header('Range', 'bytes=0-')
        if api == 'webwxgetvideo':
            request.add_header('Range', 'bytes=0-')
        try:
            response = urllib.request.urlopen(request, timeout=timeout) if timeout else urllib.request.urlopen(request)
            if api == 'webwxgetvoice' or api == 'webwxgetvideo':
                data = response.read()
            else:
                data = response.read().decode('utf-8')
            logging.debug(url)
            return data
        except urllib.error.HTTPError as e:
            logging.error('HTTPError = ' + str(e.code))
        except urllib.error.URLError as e:
            logging.error('URLError = ' + str(e.reason))
        except http.client.HTTPException as e:
            logging.error('HTTPException')
        except timeout_error as e:
            pass
        except ssl.CertificateError as e:
            pass
        except Exception:
            import traceback
            logging.error('generic exception: ' + traceback.format_exc())
        return ''

    def _post(self, url: object, params: object, jsonfmt: object = True) -> object:
        if jsonfmt:
            data = (json.dumps(params)).encode()

            request = urllib.request.Request(url=url, data=data)
            request.add_header(
                'ContentType', 'application/json; charset=UTF-8')
        else:
            request = urllib.request.Request(url=url, data=urllib.parse.urlencode(params).encode(encoding='utf-8'))

        try:
            response = urllib.request.urlopen(request)
            data = response.read()
            if jsonfmt:
                return json.loads(data.decode('utf-8'))  # object_hook=_decode_dict)
            return data
        except urllib.error.HTTPError as e:
            logging.error('HTTPError = ' + str(e.code))
        except urllib.error.URLError as e:
            logging.error('URLError = ' + str(e.reason))
        except http.client.HTTPException as e:
            logging.error('HTTPException')
        except Exception:
            import traceback
            logging.error('generic exception: ' + traceback.format_exc())

        return ''

    def _str2qr(self, _str):
        print(_str)
        qr = qrcode.QRCode()
        qr.border = 1
        qr.add_data(_str)
        qr.make()
        # img = qr.make_image()
        # img.save("qrcode.png")
        # mat = qr.get_matrix()
        # self._printQR(mat)  # qr.print_tty() or qr.print_ascii()
        qr.print_ascii(invert=True)

    def web_wx_op_log(self, type_, remark_name, user_name):
        """
        https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxoplog?lang=zh_CN&pass_ticket=tr3drarfjhmHSiZy8nfEjNVJ3QyrgtTfORvaae3I9gShx3hJeNYe5x0UmY%2BCeUEy
        type_ = 1: 群置顶: CmdId: 3; OP:1; RemarkName: (null); UserName:@@..
        type_ = 2: 取别名: CmdId: 2; RemarkName: (not null); UserName:@..
        :return:
        """
        url = self.base_uri + '/webwxoplog?lang=zh_CN&pass_ticket=%s' % (self.pass_ticket)
        if type_ == 1:
            params = {
                'BaseRequest': self.BaseRequest,
                "CmdId": 3,
                "OP": 1,
                "RemarkName": "",
                "UserName": user_name
            }
        elif type_ == 2:
            params = {
                'BaseRequest': self.BaseRequest,
                "CmdId": 2,
                "RemarkName": remark_name,
                "UserName": user_name
            }
        else:
            return
        dic_ = self._post(url, params)
        if dic_ == '':
            return False
        return dic_['BaseResponse']['Ret'] == 0

    def start_helper(self):
        """
        启动管家
        :return:
        """
        while True:
            self._run('[*] 正在获取 uuid ... ', self.get_uuid)
            self.get_QRCode()
            # 等待登陆
            time_ = 10
            is_scan = False
            while time_ > 0:
                print("wait login: {}".format(time_))
                time.sleep(1)
                time_ -= 1
                if self.wait_for_login():
                    is_scan = True
                    break
            self.wait_for_login()  # 防止用户扫描未点击登陆
            if is_scan:
                break
            else:
                return
        self._run('[*] 正在登录 ... ', self.login)
        self._run('[*] 微信初始化 ... ', self.web_wx_init)

        self._run('[*] 开启状态通知 ... ', self.web_wx_status_notify)
        self._run('[*] 获取联系人 ... ', self.web_wx_get_contact)
        self._run('[*] 获取群 ... ', self.web_wx_batch_get_contact)
        smart_log('[*] 微信网页版 ... 启动成功!')
        # threading.Thread(target=self.listen_msg_mode()).start()
        print("开启 助手：{} 成功".format(self.uin))
        self.listen_msg_mode()


class HelperStart(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None, mark=None,
                 protocol=None, web_server_token=None):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.web_server_token = web_server_token
        self.mark = mark
        global WX_HELPER_PROTO
        WX_HELPER_PROTO = protocol

    def run(self):
        super().run()
        helper = WxHelper(mark=self.mark, web_server_token=self.web_server_token)
        helper.start_helper()


class HelperStart_t(multiprocessing.Process):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, mark=None,
                 protocol=None, web_server_token=None):
        super().__init__(group, target, name, args, kwargs)
        if kwargs is None:
            kwargs = {}
        self.web_server_token = web_server_token
        self.mark = mark
        global WX_HELPER_PROTO
        WX_HELPER_PROTO = protocol

    def run(self):
        super().run()
        helper = WxHelper(mark=self.mark, web_server_token=self.web_server_token)
        helper.start_helper()


UPDATE_HELPER_GROUP_INTERVAL = 30


def update_group():
    """
    更新群信息
    :return:
    """
    pass


if __name__ == "__main__":
    start_twisted_logging('wx_helper_server')
    # qr_code_path = os.path.join(LOGIN_QRCODE_ROOT_PATH, str(datetime.datetime.now().year),
    #                             str(datetime.datetime.now().month), str(datetime.datetime.now().day))
    # print(qr_code_path.split("web")[1])

    # 每30秒更新一次获取群信息
    t = LoopingCall(update_group)  # 清除无效session
    t.start(UPDATE_HELPER_GROUP_INTERVAL)

    cpu_count = cpu_count()
    for i in range(1):
        helper_thread = HelperStart()
        helper_thread.start()
        print("第{}各helper启动成功".format(i))

    # TODO 定时存储 helper.__dict__ 到 redis； hub检查一定时间没更新的 helper 将会在其他helperServer上启动

    # new_helper = WxHelper(helper.__dict__)
    # new_helper.web_wx_get_contact()
    reactor.run()
