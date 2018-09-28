from tornado.web import RequestHandler
import json
from model import db
import math
class AdminHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("main.html")

class SearchHandler(RequestHandler):
    def post(self, *args, **kwargs):
        url = self.get_body_argument("url")
        save = self.get_body_argument("save")
        postStr = {
            "url":url,
            "save":save
        }
        self.write(postStr)

class GetfieldHnalder(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("getfield.html")

class JoblistHandler(RequestHandler):
    def post(self, *args, **kwargs):
        pagesize = self.get_body_argument("page")
        rows = self.get_body_argument("rows")
        if not pagesize:
            pagesize=1
        if not rows:
            rows=5

        model = db.Model()
        total = model.table("bossjob").count()
        jobList = model.table("bossjob").orderBy("id","desc").limit(int(pagesize),int(rows)).get()
        data = {
            "total": total['p'],
            "rows": jobList
        }
        self.write(json.dumps(data))