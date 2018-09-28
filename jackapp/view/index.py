import tornado.web
import requests
import config
from model import db
import json
import jpush

from tornado.web import RequestHandler

class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        return self.render("index/index.html")