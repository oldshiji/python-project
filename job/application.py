import tornado.web
import config
from view import index
from view import admin
class Application(tornado.web.Application):
    def __init__(self):
        headers = [
            (r"/",index.IndexHandler),
            (r"/admin",admin.AdminHandler),
            (r"/admin/search",admin.SearchHandler),
            (r"/admin/getField",admin.GetfieldHnalder),
            (r"/admin/getjoblist",admin.JoblistHandler),
        ]

        super().__init__(headers,** config.settings)