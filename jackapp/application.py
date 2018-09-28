import tornado.web
from view import index
import config

class Application(tornado.web.Application):
    def __init__(self):

        handler = [
            (r"/",index.IndexHandler),

        ]

        super(Application,self).__init__(handler,**config.settings)