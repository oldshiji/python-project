# -*- coding: utf-8 -*-
from sqlalchemy import select

from sqlalchemy import Column, DateTime, Integer, String, text, or_, ForeignKey, func, and_, BigInteger, outerjoin
from sqlalchemy.dialects.mysql import TINYINT
import datetime
import random

from common.db_model.community_db.community_db_base import CommunityBase
from common.thrift.define.ttypes import ResponseCode

__author__ = 'jerry'


class CustReply(CommunityBase):
    __tablename__ = 'CustReply'
    __table_args__ = {'schema': 'Community'}
    ReplyId = Column(Integer, primary_key=True)
    CustId = Column(Integer)
    OpenId = Column(String(50))
    Type = Column(Integer, default=1)
    Content = Column(String(255), nullable=False)
    CreateTime = Column(DateTime, nullable=False, default=datetime.datetime.now)


