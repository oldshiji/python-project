# -*- coding: utf-8 -*-
from sqlalchemy import select

from common.db_model.user_db.auth_db_base import UserBase, user_session_scope
from sqlalchemy import Column, DateTime, Integer, String, text, or_, ForeignKey, func, and_, BigInteger, outerjoin
from sqlalchemy.dialects.mysql import TINYINT
import datetime
import random

from common.thrift.define.ttypes import ResponseCode

__author__ = 'jerry'


class HelperUsers(UserBase):
    __tablename__ = 'HelperUserInfo'
    __table_args__ = {'schema': 'UserManager'}
    UserId = Column(Integer, primary_key=True, autoincrement=True)  # 产生微信用户Id
    NickName = Column(String(256))      # 用户微信昵称
    HelperUin = Column(String(45), nullable=False)
    CreateTime = Column(DateTime, nullable=False, default=datetime.datetime.now)

    @classmethod
    def delete_helper_user_info(cls, session, helper_uin):
        """
        删除助手对应客户信息
        :return:
        """
        session.query(HelperUsers).filter(HelperUsers.HelperUin == helper_uin).delete()
        return True

    @classmethod
    def get_helper_user_by_local_id(cls, session, user_id):
        """
        通过id 获取用户信息
        :param session:
        :param user_id:
        :return:
        """
        record_query = select([HelperUsers]).where(HelperUsers.UserId == user_id)
        record = session.execute(record_query).fetchone()
        return ResponseCode.Succeed, record

    @classmethod
    def get_helper_user_by_local_helper_uin(cls, session, helper_uin):
        """
        通过id 获取用户信息
        :param session:
        :param helper_uin:
        :return:
        """
        record_query = select([HelperUsers]).where(HelperUsers.HelperUin == helper_uin)
        record = session.execute(record_query).fetchone()
        return ResponseCode.Succeed, record

    @classmethod
    def create_helper_user(cls, session, nick_name, helper_uin):
        """
        创建默认密码的用户
        :param helper_uin:
        :param nick_name:
        :param session:
        :return:
        """
        # 由于一个助手服务一个客户, 先查看是否存在该助手对应的客户
        query_ = session.query(HelperUsers).filter(HelperUsers.HelperUin == helper_uin).first()
        if query_:
            return ResponseCode.Succeed, query_
        else:
            user = HelperUsers(
                NickName=nick_name,
                HelperUin=helper_uin
            )
            session.add(user)
            session.commit()
            return ResponseCode.Succeed, user

