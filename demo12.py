# -*- coding: utf-8 -*-


import sys
import time
import random
import math
import pymysql


"""

l = ['muddy','semiconductor','circuit','intelligence']

for w in l:
    print(w,len(w))
print(l)
print(l['name'])
print(l['job'])
l = {'name':'tony','age':'1000','height':'187','job':['java','node.js','VHDL','C#','Lua','SQL','FPGA']}


sorted = sorted(l)

print(sorted)

sorted1 = l.keys()


for w in sorted:
    print(l[w],'w＝',w)





print(type(l))

l = ('consult','conference','condense','constructure')

print(l)

sorted = sorted(l)

print(sorted)

for w in l:
    print(w)
    
    for w in result:
    print("ID","姓名","年龄","身高","邮件","地址")
    print(w[0],w[1],w[2],w[3],w[4],w[5])

"""


db = pymysql.connect('localhost','root','123456','py',charset='utf8')

#sql = 'show tables'
#sql = "INSERT INTO py_user(name,age,height,email,address) VALUES('zsf',10,10,'Mr.zhang@qq.com','zsf')"
#sql = """
    #INSERT INTO py_user(name,age,height,email,address)
    #VALUES ('张飞',100,100,'zhangsanfeng@sina.com','wds')
#"""


#sql = "UPDATE py_user SET name='刘备' WHERE name='张飞'"

#sql = "SELECT * FROM py_user"

#sql ="INSERT INTO py_user(name,age,height,email,address) VALUES('马化腾',10,100,'ma@qq.com','深圳')"


sql = "DELETE FROM py_user WHERE id=4"


cursor = db.cursor()

try:
    cursor.execute(sql)
    db.commit()
    #print("数据更新成功")
except:
    db.rollback()
    print('数据更新失败')


#result = cursor.fetchall()
result = cursor.rowcount

#result = cursor.fetchall()

db.close()



print(result)