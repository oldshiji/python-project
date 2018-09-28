# -*- coding: utf-8 -*-


from web.handlers.service_base_handler import ServiceBaseHandler


class CodeFileHandler(ServiceBaseHandler):

    def post(self, *args, **kwargs):
        pass

    def get(self, *args, **kwargs):
        print("req api version = {}".format(self.req_api_version))
        # path = "D:/home/server/upload/1/2017/9/16/logo.png"
        # with open(path, encoding='UTF-8') as f:
        #     self.set_header("Content-type", "image/png")
        #     self.write(f.read())





















