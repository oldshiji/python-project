# -*- coding: utf-8 -*-
from sqlalchemy import select

from sqlalchemy import Column, DateTime, Integer, String, text, or_, ForeignKey, func, and_, BigInteger, outerjoin
from sqlalchemy.dialects.mysql import TINYINT
import datetime
import random

from common.db_model.community_db.community_db_base import CommunityBase
from common.thrift.define.ttypes import ResponseCode

__author__ = 'jerry'


class CustKeywords(CommunityBase):
    __tablename__ = 'CustKeywords'
    __table_args__ = {'schema': 'Community'}
    KeyId = Column(Integer, primary_key=True)
    CustId = Column(Integer)
    OpenId = Column(String(50), nullable=False)
    ReplyId = Column(Integer)
    CreateTime = Column(DateTime, nullable=False, default=datetime.datetime.now)
    Keyword = Column(String(255))

    @classmethod
    def get_reply_by_keyword(cls, session, group_id, keyword):
        """

        :return:
        """
        from common.db_model.user_db.group_info import GroupInfo
        group_info = session.query(GroupInfo).filter(GroupInfo.GroupId == group_id).first()
        if group_info and group_info.UserId:
            from common.db_model.community_db.cust_reply import CustReply
            from common.db_model.community_db.customer_info import CustomerInfo
            record = session.query(CustKeywords, CustReply)\
                .outerjoin(CustReply, CustReply.ReplyId == CustKeywords.ReplyId)\
                .outerjoin(CustomerInfo, CustReply.CustId == CustomerInfo.CustId)\
                .filter(and_(CustomerInfo.UserId == group_info.UserId, CustKeywords.Keyword == keyword))\
                .first()
            if record:
                return record.CustReply.Content
        return None
