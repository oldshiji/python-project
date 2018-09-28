import pymysql
import view.config as config
import time

class Model(object):

    __instance = None
    def __init__(self):
        self.host = config.options['host']
        self.port = config.options['port']
        self.user = config.options['user']
        self.pwd  = config.options['pwd']
        self.dbname = config.options['dbname']
        self.charset = config.options['charset']
        self.cursor = None
        self.connection = None
        self.tableName = None
        self.fieldName = "*"
        self.orderby = ""
    def connect(self):
        try:
            self.connection = pymysql.connect(self.host,self.user,self.pwd,self.dbname,charset=self.charset)
            self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        except:
            print("数据库连接错误")
    def execute(self,sql):
        self.connect()
        self.cursor.execute(sql)
        print(self.cursor.fetchall())

    def table(self,table)->'指定数据表':
        self.tableName = table
        return self
    def save(self,data)->'保存数据':
        id = 0
        field = data.keys()
        values = data.values()
        if self.tableName == None:
            print("数据表设置一下")
            return 0
        sql = "INSERT INTO %s(%s) VALUES('%s')"%(self.tableName,",".join(field),"','".join(values))
        self.connect()
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except:
            self.connection.rollback()
            print("sql:%s运行错误"%(sql))
        self.cursor.close()
        self.connection.close()
        return self.cursor.lastrowid
    def get(self)->'获取表所有记录':
        if self.tableName==None:
            print("数据表未设置")
            return 0
        if len(self.orderby)>0:
            sql = "SELECT %s FROM %s ORDER BY %s" % (self.fieldName, self.tableName, self.orderby)
        else:
            sql = "SELECT %s FROM %s" % (self.fieldName, self.tableName)


        self.connect()
        try:
            self.cursor.execute(sql)
        except:
            print("sql：%s运行出错了"%(sql))
        return self.cursor.fetchall()

    def find(self,data)->'查询某一条或某几条记录':
        if self.tableName==None:
            print("数据表未设置")
            return 0
        if type(data) is int:
            sql = "SELECT %s FROM %s WHERE id=%d" % (self.fieldName,self.tableName, data)
        elif type(data) is list:
            idList = ",".join(data)
            sql = "SELECT %s FROM %s WHERE id IN(%s)"%(self.fieldName,self.tableName,idList)
        self.connect()
        try:
            self.cursor.execute(sql)
        except:
            print("sql:%s运行出错"%sql)

        return self.cursor.fetchall()
    def field(self,data):
        if type(data) is str:
            self.fieldName = data
        elif type(data) is list:
            self.fieldName = ",".join(data)
        return self

    def update(self,data,condition)->'数据更新':
        field = ""
        where  = ""
        result = 0
        for item in data.keys():
            field+=item+"="+"'"+data.get(item)+"'"+","

        field = field[0:-1]
        for item in condition.keys():
            where+=item+"="+"'"+condition.get(item)+"'"+" AND "

        where = where[0:-4]
        self.connect()
        sql = "UPDATE %s SET %s WHERE %s"%(self.tableName,field,where)
        try:
            result = self.cursor.execute(sql)
            self.connection.commit()
        except:
            self.connection.rollback()
            print("sql:%s运行出错"%(sql))
        self.cursor.close()
        self.connection.close()
        return result
    def delete(self,data)->"删除数据":
        where = ''
        if type(data) is int:
            sql = "DELETE FROM %s WHERE id=%s"%(self.tableName,data)
        elif type(data) is dict:
            for item in data.keys():
                where += str(item) + "=" + "'" + str(data.get(item)) + "'" + " AND "

            where = where[0:-4]
        sql = "DELETE FROM %s WHERE %s"%(self.tableName,where)
        self.connect()
        try:
            ret = self.cursor.execute(sql)
            self.connection.commit()
        except:
            print("sql:%s运行出错了"%(sql))

        self.cursor.close()
        self.connection.close()
        return ret

    def where(self,condition):
        pass
    def orderBy(self,field,sort)->'排序':
        self.orderby = str(field)+" "+str(sort)
        return self
    def limit(self,limit,offset):
        pass
    def count(self):
        pass
    def getTime(self):
        return int(time.mktime(time.gmtime(time.time())))

    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance


'''
a = db()
a.execute("select version()")
id = a.table('user').save({
    "name":"老油条33",
    "qq":"12323232",
    "add_time":str(a.getTime()),
    "login_time":str(a.getTime()),
    "ip":"2341413",
    "login_count":"1"
})
print(id)
print(a.table("user").field("name,qq").find(4))
print(a.table("user").update({
    "name":"烧耳块油条",
    "qq":"8888"
},{
    "id":"8",
    "name":"烧耳块"
}))
print(a.table("user").delete({
    "name":"老油条",
    "qq":123
}))
a = db()
print(a.table("user").orderBy("id","desc").get())

'''





