import tornado.ioloop
import tornado.web
import os
import sys
from tornado.options import define,options

class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            debug=True,
            static_path=os.path.join(os.path.dirname(__file__),'/static'),
            template_path=os.path.join(os.path.dirname(__file__),'/template')
        )

        tornado.web.Application.__init__(self,**settings)


if __name__ == '__main__':
    print("tornada server is running\r\n")
    tornado.options.parse_command_line()
    Application().listen(8888,xheaders=True)
    tornado.ioloop.IOLoop.instance().start()
