# -*- coding: utf-8 -*-
from sqlalchemy import select

from sqlalchemy import Column, DateTime, Integer, String, text, or_, ForeignKey, func, and_, BigInteger, outerjoin
from sqlalchemy.dialects.mysql import TINYINT
import datetime
import random

from common.db_model.community_db.community_db_base import CommunityBase
from common.thrift.define.ttypes import ResponseCode

__author__ = 'jerry'


class CustomerInfo(CommunityBase):
    __tablename__ = 'Customer'
    __table_args__ = {'schema': 'Community'}
    CustId = Column(Integer, primary_key=True)
    OpenId = Column(String(50))
    NickName = Column(String(50), nullable=False)
    HeadImgUrl = Column(String(255), nullable=False)
    CreateTime = Column(DateTime, nullable=False, default=datetime.datetime.now)
    UserId = Column(Integer)
    HelperToken = Column(String(45))

    @classmethod
    def get_customer_info_by_open_id(cls, session, open_id):
        """
        根据openId 获取客户信息
        :return:
        """
        if not open_id:
            return False, None
        c_info = session.query(CustomerInfo).filter(CustomerInfo.OpenId == open_id).first()
        return True, c_info

    @classmethod
    def clear_helper_with_helper_uin(cls, session, helper_uin):
        """
        清空助手
        :return:
        """
        session.query(CustomerInfo).filter(CustomerInfo.HelperToken == helper_uin) \
            .update({CustomerInfo.HelperToken: "", CustomerInfo.UserId: 0})
        return True

    @classmethod
    def set_user_id_with_helper_uin(cls, session, user_id=None, helper_uin=None):
        """
        通过uin 补充 userId
        :return:
        """
        if not user_id or not helper_uin:
            return False
        session.query(CustomerInfo).filter(CustomerInfo.HelperToken == helper_uin)\
            .update({CustomerInfo.UserId: user_id})
        return True

    @classmethod
    def set_helper_with_open_id(cls, session, open_id, user_id=None, helper_uin=None):
        """
        设置分配助手
        :return:
        """
        if not open_id:
            return False
        update_ = {}
        if user_id:
            update_.setdefault(CustomerInfo.UserId, user_id)
        if helper_uin:
            update_.setdefault(CustomerInfo.HelperToken, helper_uin)
        session.query(CustomerInfo).filter(CustomerInfo.OpenId == open_id).update(update_)
        return True

    @classmethod
    def get_customer_list(cls, session, nick_name=None, page_index=1, page_size=10):
        """
        通过id 获取用户信息
        :return:
        """
        from common.db_model.user_db.helper_info import HelperInfo
        record_query = session.query(CustomerInfo, HelperInfo).outerjoin(HelperInfo, CustomerInfo.HelperToken == HelperInfo.HelperUin)
        if nick_name:
            record_query = record_query.filter(CustomerInfo.NickName.like('%' + nick_name + '%'))
        helper_list = record_query[(page_index - 1) * page_size:page_index * page_size]
        return helper_list, record_query.count()
