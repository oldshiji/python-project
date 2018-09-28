import pymysql
"""
print(dir(pymysql))

print(help(pymysql))

print(help(pymysql.connect))
print(help(pymysql.__init__))
db = pymysql.connect('127.0.0.1','root','123456','py',charset='utf8')

cursor = db.cursor()

try:
    #sql = "desc lagou"

    sql = "select * from lagou"

    result = cursor.execute(sql)

    #print(cursor.fetchone())
    #print(cursor.fetchall())

    #print(cursor.fetchall())
    #print(cursor.fetchone())

    data = cursor.fetchone()

    #print(data[0])

    #print(data[:])

    for x in data:
        print(x)
    db.commit()
except:
    db.rollback()



db.close()
"""

