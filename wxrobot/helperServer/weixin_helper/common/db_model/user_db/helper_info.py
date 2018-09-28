# -*- coding: utf-8 -*-
from sqlalchemy import select
from sqlalchemy import update

from common.db_model.user_db.auth_db_base import UserBase, user_session_scope
from sqlalchemy import Column, DateTime, Integer, String, text, or_, ForeignKey, func, and_, BigInteger, outerjoin
from sqlalchemy.dialects.mysql import TINYINT
import datetime
import random

from common.thrift.define.ttypes import ResponseCode

__author__ = 'jerry'


class HelperInfo(UserBase):
    __tablename__ = 'HelperInfo'
    __table_args__ = {'schema': 'UserManager'}
    HelperId = Column(Integer, primary_key=True, autoincrement=True)
    HelperUin = Column(String(45), nullable=False, unique=True)
    NickName = Column(String(45))
    CreateTime = Column(DateTime, nullable=False, default=datetime.datetime.now)
    Status = Column(Integer, default=1)        # 机器人状态, 1:正常状态; 2: 离线状态
    Allocation = Column(TINYINT(1), default=0)  # 是否分配

    @classmethod
    def get_helper_info_list(cls, session, helper_uin, page_index=1, page_size=10, status=None, allocation=None):
        """
        获取助手列表
        :return:
        """
        record_query = session.query(HelperInfo)
        if helper_uin:
            record_query = record_query.filter(HelperInfo.HelperUin == helper_uin)
        if status is not None:
            record_query = record_query.filter(HelperInfo.Status == status)
        if allocation is not None:
            record_query = record_query.filter(HelperInfo.Allocation == allocation)

        helper_list = record_query.order_by(HelperInfo.CreateTime.desc())[(page_index - 1) * page_size:page_index * page_size]
        return helper_list, record_query.count()
        # if helper_uin:
        #     helper_list = record_query.filter(HelperInfo.HelperUin == helper_uin).first()
        #     return helper_list,  1 if helper_list else 0
        # else:
        #     helper_list = record_query[(page_index - 1) * page_size:page_index * page_size]
        #     count = record_query.count()
        #     return helper_list, count

    @classmethod
    def update_allocation_by_uin(cls, session, helper_uin, allocation=None):
        """
        更新助手分配状态
        :return:
        """
        if not helper_uin or allocation is None:
            return False
        session.query(HelperInfo).filter(HelperInfo.HelperUin == helper_uin)\
            .update({HelperInfo.Allocation: allocation})
        return True

    @classmethod
    def update_status_by_uin(cls, session, helper_uin, status=None):
        """
        更新助手状态
        :param session:
        :param helper_uin:
        :param status:
        :return:
        """
        if not helper_uin or status is None:
            return False
        session.query(HelperInfo).filter(HelperInfo.HelperUin == helper_uin)\
            .update({HelperInfo.Status: status})
        return True

    @classmethod
    def get_helper_info_by_uin(cls, session, uin):
        """
        通过id 获取用户信息
        :param session:
        :param uin:
        :return:
        """
        record_query = select([HelperInfo]).where(HelperInfo.HelperUin == uin)
        record = session.execute(record_query).fetchone()
        return ResponseCode.Succeed, record

    @classmethod
    def create_helper(cls, session, helper_uin, nick_name):
        """
        创建默认密码的用户
        :param nick_name:
        :param helper_uin:
        :param session:
        :return:
        """
        code, recode = cls.get_helper_info_by_uin(session=session, uin=helper_uin)
        if code == ResponseCode.Succeed and recode:
            cls.update_status_by_uin(session=session, helper_uin=helper_uin, status=1)
            return ResponseCode.Succeed, recode
        else:
            helper = HelperInfo(
                HelperUin=helper_uin,
                NickName=nick_name
            )
            session.add(helper)
            session.commit()
            return ResponseCode.Succeed, helper

