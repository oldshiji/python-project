
import pymysql;

db = pymysql.connect('localhost','root','123456','recruit');

cursor = db.cursor();

cursor.execute('show tables');

result = cursor.fetchall();

print(result);
