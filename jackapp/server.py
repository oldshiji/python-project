import tornado.ioloop
import tornado.httpserver
import config
from application import Application

if __name__=='__main__':

    app = Application()

    httpSever = tornado.httpserver.HTTPServer(app)
    httpSever.bind(config.config['port'])

    httpSever.start()


    tornado.ioloop.IOLoop.current().start()