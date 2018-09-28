# -*- coding: utf-8 -*-
import json
import uuid

import tornado
from wtforms_tornado import Form
from wtforms import PasswordField, StringField, IntegerField, FieldList
from wtforms.validators import InputRequired, Length, Optional

from common.common_setting import ADMIN_SESSION_TAG, session_dict, qr_code_map
from common.db_model.community_db.community_db_base import community_session_scope
from common.db_model.community_db.customer_info import CustomerInfo
from common.db_model.user_db.auth_db_base import user_session_scope
from common.db_model.user_db.auth_info import AuthInfo
from common.db_model.user_db.group_info import GroupInfo
from common.db_model.user_db.helper_info import HelperInfo
from common.db_model.user_db.helper_users import HelperUsers
from common.thrift.body.ttypes import HelperLoginReq
from common.thrift.define.ttypes import ResponseCode, AppId, FunctionId, DirectionType, MsgType
from common.thrift.head.ttypes import WxHead
from common.thrift_message.message import WxMessage
from web.handlers.service_base_handler import ServiceBaseHandler


class HelperHandler(ServiceBaseHandler):
    """

    """

    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        class QueryForm(Form):
            helper_uin = StringField(validators=[Optional()], default=None)
            page_index = IntegerField(validators=[Optional()], default=1)
            page_size = IntegerField(validators=[Optional()], default=10)
            status = IntegerField(validators=[Optional()], default=None)
            allocation = IntegerField(validators=[Optional()], default=None)

        form = QueryForm(self.request.arguments)

        r_list = None
        count = 0
        if form.validate():
            with user_session_scope() as session:
                r_list, count = HelperInfo \
                    .get_helper_info_list(session=session, helper_uin=form.helper_uin.data,
                                          page_index=form.page_index.data, page_size=form.page_size.data,
                                          status=form.status.data, allocation=form.allocation.data)

        self.render("helper/helper_manager.html", results=[item for item in r_list], page_index=form.page_index.data,
                    page_size=form.page_size.data, total_count=count)

    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        pass


class CustomerHandler(ServiceBaseHandler):
    """

    """

    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        class QueryForm(Form):
            nick_name = StringField(validators=[Optional()], default=None)
            page_index = IntegerField(validators=[Optional()], default=1)
            page_size = IntegerField(validators=[Optional()], default=10)

        form = QueryForm(self.request.arguments)
        r_list = None
        count = 0
        if form.validate():
            with community_session_scope() as session:
                r_list, count = CustomerInfo \
                    .get_customer_list(session=session, nick_name=form.nick_name.data,
                                       page_index=form.page_index.data, page_size=form.page_size.data)

        self.render("helper/customer_manager.html", results=[item for item in r_list], page_index=form.page_index.data,
                    page_size=form.page_size.data, total_count=count)

    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        pass


class ClearAllocationHandler(ServiceBaseHandler):
    """

    """

    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        class ClearForm(Form):
            helper_uin = StringField(validators=[InputRequired()])

        form = ClearForm(self.request.arguments)
        if form.validate():
            with user_session_scope() as session:
                b_ = CustomerInfo.clear_helper_with_helper_uin(session=session, helper_uin=form.helper_uin.data)
                b1_ = HelperInfo.update_allocation_by_uin(session=session, helper_uin=form.helper_uin.data,
                                                          allocation=0)
                b2_ = HelperUsers.delete_helper_user_info(session=session, helper_uin=form.helper_uin.data)
            if b_ and b1_ and b2_:
                self.write({"code": 1})
        else:
            self.write({"code": 2})


class AllocationHandler(ServiceBaseHandler):
    """
    分配助手处理
    """

    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        with user_session_scope() as session:
            r_list, count = HelperInfo \
                .get_helper_info_list(session=session, helper_uin=None,
                                      page_index=1, page_size=10,
                                      status=1, allocation=0)
            self.write(json.dumps(
                [{"HelperId": item.HelperId, "HelperUin": item.HelperUin, "NickName": item.NickName} for item in
                 r_list]))

    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        class SetForm(Form):
            open_id = StringField(validators=[InputRequired()])
            helper_uin = StringField(validators=[InputRequired()])

        form = SetForm(self.request.arguments)
        if form.validate():
            with user_session_scope() as session:
                b_ = CustomerInfo.set_helper_with_open_id(session=session, open_id=form.open_id.data, user_id=None,
                                                          helper_uin=form.helper_uin.data)
                b1_ = HelperInfo.update_allocation_by_uin(session=session, helper_uin=form.helper_uin.data,
                                                          allocation=1)
            if b_ and b1_:
                self.write({"code": 1})
        else:
            self.write({"code": 2})


class CustomerSendMessageHandler(ServiceBaseHandler):
    """
    http://101.132.245.172:8090/customer/send/message?open_id=sf&content=sagas&msg_type=1&group_id=1&group_id=2
    发送消息
    """

    def post(self, *args, **kwargs):

        open_id = self.get_argument("open_id")
        content = self.get_argument("content")
        msg_type = self.get_argument("msg_type", MsgType.MsgType_Text)
        group_id_list = self.get_argument_array("group_id")

        if open_id and content and msg_type and group_id_list and len(group_id_list) > 0:
            from web.utils.web_access_linker import WEB_ACCESS_LINKER_PROTOCOL
            WEB_ACCESS_LINKER_PROTOCOL.send_msg_to_wx_helper(open_id=open_id, content=content,
                                                             group_id_list=group_id_list, msg_type=msg_type)

            self.write({"code": 1, "msg": "已发送"})
        else:
            self.write({"code": 2, "msg": "参数异常"})


class RegisterHelperHandler(ServiceBaseHandler):
    """
    注册助手
    """

    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        class QueryForm(Form):
            mark = StringField(validators=[InputRequired()])

        form = QueryForm(self.request.arguments)
        if form.validate():
            code_url = qr_code_map.get(form.mark.data)
            self.write({"code": 1, "msg": code_url})
        else:
            self.write({"code": 2, "msg": "系统参数异常"})

    @tornado.web.authenticated
    def post(self, *args, **kwargs):

        from web.utils.web_access_linker import WEB_ACCESS_LINKER_PROTOCOL
        head_ = WxHead()
        head_.appId = AppId.AppType_HelperServer
        head_.functionId = FunctionId.HelperServer_HelperLogin
        head_.direction = DirectionType.ToWxServer

        head_.tag = 2
        head_.serverTokenId = WEB_ACCESS_LINKER_PROTOCOL.get_server_token_id()
        head_.mark = str(uuid.uuid4())
        req = HelperLoginReq()
        WEB_ACCESS_LINKER_PROTOCOL.send_msg(head=head_, body=req)
        self.write({"code": 1, "mark": head_.mark})


class GroupHandler(ServiceBaseHandler):
    """

    """

    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        class QueryForm(Form):
            open_id = StringField(validators=[Optional()])
            page_index = IntegerField(validators=[Optional()], default=1)
            page_size = IntegerField(validators=[Optional()], default=10)

        form = QueryForm(self.request.arguments)
        r_list = None
        count = 0
        if form.validate():
            with user_session_scope() as session:
                r_list, count = GroupInfo.get_group_list(session=session, page_index=form.page_index.data,
                                                         page_size=form.page_size.data, open_id=form.open_id.data)

        self.render("helper/group_manager.html", results=[item for item in r_list], page_index=form.page_index.data,
                    page_size=form.page_size.data, total_count=count, open_id=form.open_id.data)

    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        class SetForm(Form):
            open_id = StringField(validators=[InputRequired()])
            helper_uin = StringField(validators=[InputRequired()])
            buy_count = IntegerField(validators=[InputRequired()])
        form = SetForm(self.request.arguments)
        if form.validate() and form.buy_count.data > 0:
            with user_session_scope() as session:
                from common.db_model.community_db.customer_info import CustomerInfo
                b_, customer_info = CustomerInfo.get_customer_info_by_open_id(session=session, open_id=form.open_id.data)
                user_id = None
                if b_ and customer_info:
                    user_id = customer_info.UserId
                for index in range(form.buy_count.data):
                    GroupInfo.init_group(session=session, helper_uin=form.helper_uin.data, open_id=form.open_id.data,
                                         user_id=user_id)
            self.write({"code": 1, "msg": "已分配"})
        else:
            self.write({"code": 1, "msg": "参数异常"})



