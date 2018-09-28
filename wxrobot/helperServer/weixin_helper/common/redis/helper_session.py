# -*- coding: utf-8 -*-

import redis, json

from common.common_setting import Redis_IP, Redis_Port, Redis_Passwd

pool = redis.ConnectionPool(host=Redis_IP, port=Redis_Port, password=Redis_Passwd, db=1)


class HelperSession(redis.StrictRedis):
    """
    存储管家处于哪个服务节点上
    """
    helper_token = ""
    helper_server_token = ""

    def __init__(self, helper_token, helper_server_token):
        global pool
        super().__init__(connection_pool=pool)
        self.helper_token = helper_token
        self.helper_server_token = helper_server_token

    def save_helper(self):
        """
        保存对象信息
        :return:
        """
        if not self.helper_token or not self.helper_server_token:
            return None
        self.set(name=self.helper_token, value=self.helper_server_token)

    def get_server_token_by_helper_token(self):
        """
        根据
        """
        if not self.helper_token:
            return None
        self.helper_server_token = self.get(self.helper_token)

    def delete_server_relation_by_helper_token(self):
        if not self.helper_token:
            return None
        self.delete(self.helper_token)


if __name__ == "__main__":
    s = HelperSession(helper_token="test1", helper_server_token=None)
    # s.save_helper()

    s.get_server_token_by_helper_token()

    print(s)


