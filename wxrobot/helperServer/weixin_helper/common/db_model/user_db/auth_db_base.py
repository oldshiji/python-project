# -*- coding: utf-8 -*-


__author__ = 'jerry'

import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager
from common.common_setting import SQL_DB_CONNECTION_STR

UserBase = declarative_base()
user_metadata = UserBase.metadata

user_engine = create_engine(SQL_DB_CONNECTION_STR + "/UserManager?charset=utf8", pool_size=5,
                            pool_recycle=3600)


@contextmanager
def user_session_scope():
    """Provide a transactional scope around a series of operations."""
    session = sessionmaker(bind=user_engine, expire_on_commit=False)()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        logging.exception(e)
        raise
    finally:
        session.close()
