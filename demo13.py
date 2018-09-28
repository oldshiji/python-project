# -*- coding: utf-8 -*-
import pymysql

db = pymysql.connect('localhost','root','123456','py',charset='utf8')
cursor = db.cursor()

sql = "SELECT * FROM py_user"
cursor.execute(sql)
result = cursor.fetchall()
result = sorted(result)
print(result)

db.close()