import pymysql.cursors


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='py',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor
                             )





try:

    with connection.cursor() as cursor:

        sql = "select * from lagou limit 1"

        cursor.execute(sql)

        print(cursor.fetchone())





except:
    print(cursor.Error)


finally:
    connection.close()