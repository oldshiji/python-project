import pymysql

connect = pymysql.connect("127.0.0.1","root","123456","webim",charset='utf8')

cursor = connect.cursor()

cursor.execute("show tables")

print(cursor.fetchone())