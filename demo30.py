import time

#print(time.strftime('%Y-%m-%d',time.localtime(time.time())))

a = 'hello,world'



""""
str(a)

repr(a)

str(1/7)

x = 3.1415926
y = 32.98

s = "this value of x is"+repr(x)+",the value of y is:"+repr(y)
s1 = "this value of x is"+x+",this value of y is:"+y

print(s)
print(s1)

hello = "hello,world\n"
hells = repr(hello)
hellos = str(hello)

print(hells)
print(hello)
print(hellos)
print(repr((3.23,4.56,(1,2))))
for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3),end='')
    print(repr(x*x*x).rjust(4))
    
for x in range(1,11):
    print(repr(x),repr(x*x),end='')
    print(repr(x*x*x))


for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3),end='')
    print(repr(x*x*x).rjust(4))
    
for x in range(1,11):
    print('{0:2d},{1:3d},{2:4d}'.format(x,x*x,x*x*x))


for y in range(1,11):
    print('{0:1d} {1:1d},{2:1d}'.format(y,y*y,y*y*y))

for z in range(1,11):
    print('{0} {1},{2}'.format(z,z*z,z*z*z))
"""

print("当前登录用户名：" + repr(123) + ",文件的创建时间：" + repr(time.time()) + "，文件名：" + repr(234))