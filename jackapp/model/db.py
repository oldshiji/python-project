import pymysql
import config
import sys

class db():


    def __init__(self):

        self.host    = config.dbconfig['host']
        self.port    = config.dbconfig['port']
        self.user    = config.dbconfig['user']
        self.pwd     = config.dbconfig['pwd']
        self.dbname  = config.dbconfig['dbname']
        self.charset = config.dbconfig['charset']



    def connect(self):

        self.connector = pymysql.connect(self.host,self.user,self.pwd,self.dbname,charset=self.charset)
        self.cursor = self.connector.cursor()
    def getInstance(self):

        if not isinstance(self.instance,self):
            self.instance = self()


        return self.instance
    def get(self):
        sql = "SELECT * FROM im_user LIMIT 1"
        self.connect()
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        print(result)
        result = ''
        try:
            self.connect()
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            print(result)
        except:
            sys.stderr.write(sql+str("语句错误"))

