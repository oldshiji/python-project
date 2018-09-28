import time

#print(time.time())
#print(time.strftime('%Y-%m-%d',time.localtime(time.time())))
""""
a = 'responsibility'
b = "responsibility"
c = '''responsibility'''

e = r'c:\test.txt'
f = b'sp\0xam'


print(type(a,b,c,d))
a = 'hello','world'
print(a)
a = 'hello"s'
print(a)
a = "hello's"
print(a)
a = 'hellow' 'world'
b = 'hello','world'
print(a)
print(b)
a = 'chinese','japanese','america'
b = "hello" "world" "rejoice"

print(a)
print(b)
a = "hello's","world's"
b = "hello\'s","world\'s"

print(a,b)
f = open("new\text.txt","r")

result = f.read(100)
print(result)
f.close()
a = 
import os
os.getcwd()


print(a)
a = 'abc'
b = 'def'
c = a+b
print(c)
print(len(c))
print('hello'*10)
print('-'*100)
print('hello,world')
print(time.time())
print('*'*100)
a = "chinese"
print(a)
for i in a:
    print(i,end='')
    a = "chinese"
print('a' in a)
print('c' in a)
print(a[1],a[-1])
print(a[1:3])
print(a[1:])
print(a[1:-1])
print(a[-1:2])
a = "chinese"

print(a[0:-1:2])
print(a[0:-1:3])
print(a[0:-1:1])
print(len(a))

print(a[:])
print(a[1:26])
print(a[0:])
print(a[:-1])

print(a[:])
print(a[::1])
print(a[::2])
print(a[0:-1:1])
print(a[0:-1:2])
print(a[0:-1:3])
a = "abcdefghijklmnopqrstuvwxyz"



print(a[::-1])
print(a[::-2])
print(int('42'),str(42))

print(str('spam'),repr('spam'))
print(type(a),type(b))

c = a+b
print(c)
a = '42'
b = 1

c = int(a)+b
d = a+str(b)

print(c,d)
print(str("3."))
print(ord('a'))
print(ord('A'))
print(chr(97))
s = "chinese"
s[0]= 'j'
print(s)
s = "chinese"
s = 'j'+s[1:]
print(s)
s = "chinese"
s = s[0:4]+'a'
print(s)

s = "chinese"
print(s.replace('ese','a'))

1、字符串写法
２、字符串基本操作
+　*
３、字符串索引，分片操作
４、字符串修改操作
５、字符串格式化
６、字符串转码操作
a = "this is %s bird" %('dead')
b = "this is {0}'s bird".format("dead")
print(a,b)
a ="xxxxchinesexxxxxxxchinese"

#print(a.find("chinese"))
where = a.find("chinese")

a = a[:where]+"japanese"+a[where+7:]

print(a)
a ="xxxxchinesexxxxxxxchinese"

print(a)
print(a.replace("chinese","japanese"))

print(a.replace("chinese","japanese",1))
print(a)

for x in a:
    print(x)
    
    
for i in 
a = "chinese"

a = list(a)

a[0] = "j"
a[1] = "p"

print(a)

print(''.join(a))
print("chinese".join(['japanese','america','franch','peninsula']))
a ="aaa bbb ccc"
col1 = a[:3]
col2 = a[8:]

print(col1,col2)

print(a.split())
a = "aaa,bbb,ccc"

print(a.split(","))

print(a)
print(a)
print(a.rstrip())
print(a.upper())
print(a.isalpha())
print(a.endswith("Ni\n"))
print(a.startswith("The"))
a ="The knife who say Ni\n"


print("the" in a)

print(a.find("Ni")!=-1)

sub = a[:3]

print(sub in a)
examtion = "NI"

a = "The knife who say %s" %(examtion)

print(a)

a = "%d %s %d" % (10,'and',20)
print(a)

x = 1234
print("%d--%-6d--%06d" % (x,x,x))
print("%e--%f--%g" % (x,x,x))
x = 1.23456789

print("%06f--%-6f--%+6f"%(x,x,x))
a = "there are %(num)d dogs and %(name)s" % {"num":100,"name":'dogs'}
print(a)

replay = 
Hello,%(name)s
Your squeeze is %(age)d


value = {"name":'tony',"age":100}

print(replay % value)
food = "apple"
quarterly = 8

print(vars())
"""


food = "apple"
quarterly = 8

print("%(food)s---%(quarterly)d" % vars())

