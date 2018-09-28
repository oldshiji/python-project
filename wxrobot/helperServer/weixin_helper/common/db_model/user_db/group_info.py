# -*- coding: utf-8 -*-
from sqlalchemy import select, Text

from common.db_model.user_db.auth_db_base import UserBase, user_session_scope
from sqlalchemy import Column, DateTime, Integer, String, text, or_, ForeignKey, func, and_, BigInteger, outerjoin
from sqlalchemy.dialects.mysql import TINYINT
import datetime
import random

from common.thrift.define.ttypes import ResponseCode

__author__ = 'jerry'


class GroupInfo(UserBase):
    """
    群信息
    """
    __tablename__ = 'GroupInfo'
    __table_args__ = {'schema': 'UserManager'}
    GroupId = Column(Integer, primary_key=True)
    HelperUin = Column(String(45), nullable=False)
    HelperGroupShowName = Column(String(45))  # 群显示名称(结合 HelperUin 来标识唯一群)
    UserId = Column(Integer)  # 群归属哪个用户, 该ID 为本平台生成
    OpenId = Column(String(50))  # 群归属微信公众号OpenId
    UserName = Column(String(128))  # 群的微信标识
    NickName = Column(String(255))  # 用户昵称
    BuyData = Column(DateTime, default=datetime.datetime.now)
    ExpireData = Column(DateTime)
    Status = Column(TINYINT(1), default=1)  # 状态. 1:默认状态, 2：开通状态
    OtherAttrJson = Column(Text)  # 群其他属性
    GroupName = Column(String(255))

    @classmethod
    def update_asy_group_info(cls, session, group_id, user_name, status=1, other_json=None, helper_show=None,
                              group_name=None, user_id=None):
        """
        更新开通群信息
        :return:
        """
        if not group_id:
            return False
        update_ = {}
        if user_name:
            update_.setdefault(GroupInfo.UserName, user_name)
        if status:
            update_.setdefault(GroupInfo.Status, status)
        if other_json:
            update_.setdefault(GroupInfo.OtherAttrJson, other_json)
        if helper_show:
            update_.setdefault(GroupInfo.HelperGroupShowName, helper_show)
        if group_name:
            update_.setdefault(GroupInfo.GroupName, group_name)
        if user_id:
            update_.setdefault(GroupInfo.UserId, user_id)

        session.query(GroupInfo).filter(GroupInfo.GroupId == group_id) \
            .update(update_)
        return True

    @classmethod
    def get_group_list_by_group_id_list(cls, session, group_id_list):
        """
        获取群信息
        :return:
        """
        if session and group_id_list and len(group_id_list) > 0:
            return session.query(GroupInfo).filter(GroupInfo.GroupId.in_(group_id_list)).all()
        else:
            return None

    @classmethod
    def init_group(cls, session, helper_uin=None, open_id=None, user_id=None):
        """
        保存群信息, 需要检测
        :return:
        """
        if not helper_uin or not open_id:
            return False, None
        group_info = GroupInfo(HelperUin=helper_uin, OpenId=open_id, UserId=user_id)
        session.add(group_info)
        session.commit()
        return True, group_info

    @classmethod
    def get_group_list(cls, session, page_index=1, page_size=10, open_id=None):
        """
        获取群列表
        :return:
        """
        record_query = session.query(GroupInfo)
        if open_id:
            record_query = record_query.filter(GroupInfo.OpenId == open_id)
        helper_list = record_query[(page_index - 1) * page_size:page_index * page_size]
        return helper_list, record_query.count()
