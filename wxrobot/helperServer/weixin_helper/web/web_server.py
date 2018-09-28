# -*- coding: utf-8 -*-
import os.path

import tornado.auth
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.netutil
import tornado.process
from tornado.options import define, options
from tornado.web import url

from common.common_setting import DEVELOP

import web.handlers.test.code_handler as test
import web.handlers.index.login_handler as login
import web.handlers.helper.helper_handler as helper
from web.handlers.modules_handler import Paginator
from web.handlers.service_base_handler import PageNotFoundHandler
from web.utils.web_access_linker import web_access_initialize

__author__ = 'jerry'

define("port", default=8090, help="run on the given port", type=int)
define('debug', default=True, help="run in debug mode (with automatic reloading)")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            # ========================== 顶级接口 ==========================
            #
            # url(r"/([0-9]*)([/]*)([a-z]*)", test.CodeFileHandler, name='data_receive'),
            url(r"/", login.IndexHandler, name='index'),
            url(r"/login", login.LoginHandler, name='login'),
            url(r"/helper/manager", helper.HelperHandler, name='helper_manager'),
            url(r"/helper/allocation", helper.AllocationHandler, name='helper_allocation'),
            url(r"/clear/allocation", helper.ClearAllocationHandler, name='clear_allocation'),
            url(r"/customer/helper/manager", helper.CustomerHandler, name='customer_helper_manager'),
            url(r"/customer/group/manager", helper.GroupHandler, name='customer_group_manager'),
            url(r"/register/helper", helper.RegisterHelperHandler, name='register_helper'),

            url(r"/customer/send/message", helper.CustomerSendMessageHandler, name='customer_send_message'),
            ('.*', PageNotFoundHandler)
        ]
        ui_modules = {'Paginator': Paginator}
        settings = dict(
            ui_modules=ui_modules,
            cookie_secret="c808bf19-f9d9-11e4-a903-ac87a32f4e4c",
            login_url="/login",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=False,
            debug=options.debug,
            autoescape=None,
        )
        tornado.web.Application.__init__(self, handlers, **settings)


def main():

    web_access_initialize()

    tornado.options.parse_command_line()
    options.debug = DEVELOP
    options.log_to_stderr = False
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    print('cerium_web_server 启动在 http://localhost:%d 点击访问' % options.port)

    # 当前文件的文件夹
    # current_path = os.path.dirname(os.path.abspath(__file__))
    # dist_file = os.path.join(current_path, 'config/loggingConf_time.yaml')
    # logging.config.dictConfig(yaml.load(open(dist_file, 'r')))  # 日志配置

    tornado.ioloop.IOLoop.current().start()


def simple_asyn_main():
    """
    simple multi-process
    :return:
    """
    tornado.options.parse_command_line()
    # 需要关闭 德不孤模式 否则: Cannot run in multiple processes: IOLoop instance has already been initialized. You cannot call
    # IOLoop.instance() before calling start_processes()
    options.debug = False
    options.log_to_stderr = False

    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.bind(options.port)
    http_server.start(0)  # Forks multiple sub-processes
    print('web_server 启动在 http://localhost:%d 点击访问' % options.port)
    tornado.ioloop.IOLoop.current().start()


def advanced_asyn_main():
    """
    advanced multi-process
    :return:
    """
    tornado.options.parse_command_line()
    options.debug = DEVELOP
    options.log_to_stderr = False

    sockets = tornado.netutil.bind_sockets(options.port)
    tornado.process.fork_processes(0)
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.add_sockets(sockets)
    print('web_server 启动在 http://localhost:%d 点击访问' % options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
