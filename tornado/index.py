import tornado.ioloop
import tornado.web

class MainHander(tornado.web.RequestHandler):
    def get(self):
        self.write("hello,world")




application = tornado.web.Application([
    (r'/',MainHander)
])


if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()