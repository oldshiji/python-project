# -*- coding: utf-8 -*-
from sqlalchemy import select

from common.db_model.user_db.auth_db_base import UserBase, user_session_scope
from sqlalchemy import Column, DateTime, Integer, String, text, or_, ForeignKey, func, and_, BigInteger, outerjoin
from sqlalchemy.dialects.mysql import TINYINT
import datetime
import random

from common.thrift.define.ttypes import ResponseCode

__author__ = 'jerry'


class AuthInfo(UserBase):
    __tablename__ = 'AuthInfo'
    __table_args__ = {'schema': 'UserManager'}
    AuthId = Column(Integer, primary_key=True)
    LoginName = Column(String(45))
    Passwd = Column(String(45), nullable=False)
    CreateTime = Column(DateTime, nullable=False, default=datetime.datetime.now)
    Status = Column(Integer, default=1)

    @classmethod
    def get_auth_info_by_login_name_password(cls, session, login_name, password):
        """
        通过id 获取用户信息
        :param password:
        :param login_name:
        :param session:
        :param user_id:
        :return:
        """
        record_query = select([AuthInfo]).where(and_(AuthInfo.LoginName == login_name, AuthInfo.Passwd == password))
        record = session.execute(record_query).fetchone()
        if not record:
            return ResponseCode.Failed, None
        return ResponseCode.Succeed, record

    @classmethod
    def get_auth_info_by_auth_id(cls, session, auth_id):
        """

        :param session:
        :param auth_id:
        :return:
        """
        record = session.query(AuthInfo).filter(AuthInfo.AuthId == auth_id).first()
        if not record:
            return ResponseCode.Failed, None
        return ResponseCode.Succeed, record


