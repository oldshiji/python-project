
#单行开头
print("+hello world\r\n")
#多行开头
print("$11\r\nhello world\r\n")
print(len("hello world"))
#数值
print(":1024\r\n")
#错误
print("-WrongType there are some error\r\n")
#array
print("*3\r\n:1\r\n:2\r\n:3\r\n")
#NULL
print("$-1\r\n")
#0
print("$0\r\n\r\n")
#set age 100
#数组形式　　拆分为多行字符串
'''
set 多行字符串　表示：$3\r\nset\r\n
age 多行字符串　表示：$3\r\nage\r\n
age 数字　　　　表示：:100\r\n
*3\r\n$3\r\nset\r\n$3\r\nage\r\n:100\r\n
'''


a = "*3\r\n$3\r\nset\r\n$3\r\nage\r\n:100\r\n"
print(a)

b = "jack"
print(type(b) is str)