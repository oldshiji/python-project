# -*- coding: utf-8 -*-
import uuid

import tornado
from wtforms_tornado import Form
from wtforms import PasswordField, StringField
from wtforms.validators import InputRequired, Length, Optional

from common.common_setting import ADMIN_SESSION_TAG, session_dict
from common.db_model.user_db.auth_db_base import user_session_scope
from common.db_model.user_db.auth_info import AuthInfo
from common.thrift.define.ttypes import ResponseCode
from web.handlers.service_base_handler import ServiceBaseHandler


class LoginHandler(ServiceBaseHandler):
    """
    处理登录请求
    """

    def post(self, *args, **kwargs):
        class AuthLoginForm(Form):
            username = StringField(validators=[InputRequired(), Length(max=32)])
            password = PasswordField(validators=[InputRequired(), Length(min=6, max=60)])
            next_page = StringField(validators=[Optional()])

        form = AuthLoginForm(self.request.arguments)
        if form.validate():
            username = form.username.data
            password = form.password.data
            with user_session_scope() as session:
                code, record = AuthInfo.get_auth_info_by_login_name_password(session=session, login_name=username,
                                                                             password=password)
            if code == ResponseCode.Succeed and record:

                token_id = str(uuid.uuid4())
                session_dict.setdefault(token_id, {"AuthId": record.AuthId, "LoginName": record.LoginName,
                                                   "Status": record.Status})

                self.set_secure_cookie(ADMIN_SESSION_TAG, token_id)
                if form.next_page and form.next_page.data:
                    self.redirect(form.next_page.data)
                else:
                    self.redirect('/')
            else:
                self.render('index/login.html', next_page=form.next_page.data, msg='登录失败')
        else:
            self.render('index/login.html', next_page=form.next_page.data, msg='密码不合规范')

    def get(self, *args, **kwargs):
        if self.current_user:
            self.redirect('/')
        else:
            next_page = self.get_argument('next', None)
            self.render('index/login.html', next_page=next_page)


class IndexHandler(ServiceBaseHandler):
    """

    """

    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render("default/index.html")

    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        pass
