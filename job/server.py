import tornado.web
import tornado.ioloop
import tornado.httpserver
import config
from application import Application
if __name__ == '__main__':

    app = Application()
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.listen(config.options['port'],config.options['address'])
    httpServer.start()
    tornado.ioloop.IOLoop.current().start()