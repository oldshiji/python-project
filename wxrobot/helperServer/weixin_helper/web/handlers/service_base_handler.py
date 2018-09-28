# -*- coding: utf-8 -*-
import tornado
from tornado.web import RequestHandler, HTTPError

from tornado.escape import utf8

import json
import datetime

from common.common_setting import ADMIN_SESSION_TAG, session_dict

__author__ = 'jerry'


def date_handler(obj):
    if isinstance(obj, datetime.datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    else:
        return obj


class PageNotFoundHandler(RequestHandler):
    def get(self):
        raise tornado.web.HTTPError(404)


class ServiceBaseHandler(RequestHandler):
    req_api_version = 1
    req_api_type = 'pb'

    def data_received(self, chunk):
        pass

    # def prepare(self):
    #     token_id = self.get_cookie(WEB_SESSION_TAG)
    #     session = MGSession.create_anonymous_or_update(self.request.remote_ip, Web, token_id)
    #     if session:
    #         self.set_cookie(WEB_SESSION_TAG, session.token_id)

    def get_current_user(self):
        token_id = self.get_secure_cookie(ADMIN_SESSION_TAG)
        if token_id:
            auth_info = session_dict.get(str(token_id, encoding="utf8"))
            return auth_info
        else:
            return None

    def render(self, template_name, **kwargs):
        if self.current_user:
            kwargs['avatar_url'] = ""
            kwargs['file_site_url'] = None
            kwargs['user'] = self.current_user
            kwargs['article_count'] = 0
            kwargs['strategy_count'] = 0
            kwargs['news_count'] = 0
        if 'msg' not in kwargs:
            kwargs['msg'] = None
        super(ServiceBaseHandler, self).render(template_name, **kwargs)

    def get_argument_array(self, name, strip=True):
        """
        自定义兼容特殊数组参数的函数（如label_list[0]=a&label_list[1]=b）
        :param name:
        :param strip:
        :return:
        """
        arg_array = self.get_arguments(name, strip)
        if not arg_array:
            if '[]' in name:
                arg_array = []
                name_format = name.replace('[]', '[{}]')
                for i in range(len(self.request.arguments)):
                    arg = self.get_argument(name_format.format(i), None)
                    if arg:
                        arg_array.append(arg)
                    else:
                        break
        return arg_array

    def prepare(self):
        super().prepare()

    def write_resp(self, chunk, callback=None):
        """
        将各种数据写入相应流
        :param chunk: 数据
        :param callback: 回调字符串
        :return:
        """
        if self.req_api_type == 'pb':
            self.write(chunk.SerializeToString())
        else:
            raise HTTPError(405)

    def write_jsonp(self, callback, chunk):
        """
        将jsonp字符串写入返回流
        :param callback: 请求传过来的callback值
        :param chunk: json字符串或者是dict类型
        """
        if isinstance(chunk, dict):
            chunk = json.dumps(chunk, default=date_handler)
        chunk = utf8(chunk)
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.write("{}({})".format(callback, chunk))
