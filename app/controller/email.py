import pymysql

def getOne(id)->'操作数据库获取一条数据':

    db = pymysql.connect('localhost','root','123456','py',charset='utf8')
    cursor = db.cursor()

    if id:
        sql = "%s=%d" % ("select * from py_user where id", id)
    else:
        exit("参数错误")

    try:

        result = cursor.execute(sql)
        db.commit()

    except:
        db.rollback()



    db.close()
    return cursor.fetchone()
    return sql



#print('%s=%d' %('hello',20))




