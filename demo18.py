import time
import pymysql

l = ['muddy','accordance','canteen','sketch']

""""
print(l)

print(l[0])  #取第一个
print(l[0:3])　#从０取３个
print(l[:]) #从０取到最后一个
print(l[0:]) #同上
print(l[:3])　#从０取３个

for w in l:
    print(w,len(w),w.upper(),w.isdecimal())
    
for i in range(10):
    print(i,i.bit_length()) 
    
a = 0o12  # 转换为１０进制　　1*　　　８的１次方为８＝１*８+２
b = 0x15　#　１*１６+５
c = 0b1100　#８+４
print(a,b,c)
i = 30

print(oct(i),hex(i),bin(i))

a = ['memorial','joice','nodiy']

for i in range(len(a)):
    print(i,a[i])
    print(range(10))
print(list(range(10)))
a = ('melt','range','present')

print(a)
print(type(a))
print(len(a))
print(list(a))
print(a[0])

for i in a:
    print(i)
    
for n in range(10):
for x in range(2,n):
    if n%x == 0:#8 % 2 8%3 8%4 8%5 8%6 8%7 8%8
        print(n,'=',x)
        break
else:
    print(n)

for i in range(10):
    if i%2==0:
        print(i)
        continue
while True:
pass


def f(n):
    a,b=0,1
    while a<n:#n=10 0<10  1<10 1<10 2<10 3<10
        #print(a,b)
        print(a,end='')
        a,b=b,a+b  #a=1,b=1  a=1 b=2 a=2 b=3  a=3 b=5 a=5 b=8

    print()

#f(2000)

fun = f

print(fun(100))
def f1(n):
    result = []
    a,b=0,1
    while a<n:
        result.append(a)
        a,b=b,a+b

    return result

r = f1(200)

print(r)
def f2(n):
    a=n


print(f2(3))#py默认会返回一个内置的None值
def f3(n):
    a=n



print(f3(100))
#print(a)
#print(n)

def f4(n):
    return n


print(f4(100))
def l(a,L=[]):
    L.append(a)
    return L


print(l(1))
print(l(2))
print(l(3))

def l(a,L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(l(1))
print(l(2))
print(l(3))

def showmsg(title,content='是否要处理这条记录',type='comment'):
    print('windows of title is:',title)
    print('content is:',content)
    print('windows of type is:',type)


#showmsg('提示信息')
#showmsg('操作提示',content='是否要处理这条数据',type='评论')

#showmsg()# 缺少参数title
#showmsg(title='温馨提示')
#showmsg('提示信息','是否要删除本条记录','处理流程')

#showmsg(title='系统提示',content='是否要清理',type='清理')

#showmsg(title='用户信息')

#showmsg('userinfo','dead')

#showmsg(110,title=200)

showmsg(action='element')

def function(a):
    print('input params a of value is:',a)


function(0,a=100)

def function1(kind,*arguments,**job):
    print("关键字参数字接收kind:",kind)
    for w in arguments:
        print("关键字参数接收元组arguments:",w)
    #r = sorted(job)
    r = sorted(job.keys())
    for k in r:
        print(k,"关键字参数接收字典job:",job[k])


function1('villance','wash your brain',name='tony',age=100,address='beijing')

默认参数
可选参数
位置参数
关键字参数
可变参数

def write_multipart_line(file,separator,*args):
    file.write(separator.join(args))
    print(file)
    print(separator)
    print(args)
    #print(type(args))



f = open("test1.txt",mode='w',encoding='utf8')

write_multipart_line(f,"-","wash your pen","doing something")

def fileputcontent(file,separator,**args):

    #r = sorted(args)
    file.write(separator.join(args))



f = open("test2.txt",mode='w',encoding='utf8')
fileputcontent(f,'/',key1='value1',key2='value2')
def separator(*args,sep):
    return sep.join(args)


print(separator('do to something at sometime','doing',sep='/'))

print(list(range(3,6)))

a = [3,6]

print(list(range(*a)))

print(*a)

a ={'name':'tony','age':'100','address':'shanghai'}

print(a)
print(**a)

def incrs(n):
    return lambda x:x+n


f = incrs(10)

print(f(1))

print(f(2))

key = lambda x:x+10


x = function(x){
    return x+10
}

key = lambda x:x+10


print(type(key))
print(key(10))



address = lambda adds,where:'your address is:'+adds+where

print(address)

print(address('shanghai','beijing'))
#result = db("select * from py_user",type='get')
#result = db("insert into py_user(name,age,height,email,address) values('刘德华','60','120','liu@sina.com','hongkong')",type='insert')
#result = db("update py_user set name='张三丰' where id=10",type='update')
result = db("delete from py_user where id=10",type='delete')

def db(sql,type):
    db = pymysql.connect('localhost','root','123456','py',charset='utf8')
    cursor = db.cursor()
    try:
        result = cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    if type =='get':
        return cursor.fetchall()
    elif type == 'insert':
        #return cursor.rowcount
        return cursor.lastrowid
    elif type == 'delete':
        return db.affected_rows()
    elif type == 'update':
        return db.affected_rows()



"""


class DB:
    table = ''
    field = ''
    where = ''
    cursor = ''
    sql = ''
    def __init__(self,table=''):
        db = pymysql.connect('localhost','root','123456','py',charset='utf8')
        self.cursor = db.cursor()
        self.table = table
        #return self
    def table(self,table):
        self.table = table
        #return self
    def field(self,field=[]):
        self.field = ",".join(field)
        #return self
    def finddata(self):
        self.sql =  "select "+self.field+" from "+self.table+" limit 1"
        return self.sql

#result = DB().table("py_user").field("name,age").find()
result = DB()

lists = result.finddata


print(lists())

