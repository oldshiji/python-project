

""""
#基本赋值

a = 'chinese'
print(a)
#元组赋值

a,b,c = '123'
print(a,b,c)
(a,b,c) = (1,2,3)
print(a,b,c)

((a,b),c) = ((1,2),4)
print(a,b,c)

a,b,c = [1,2,3]
print(a,b,c)

string = 'abc'

(a,b,c) = string
print(a,b,c)
string = 'chinese'
a,b,c = string
print(a,b,c)
string = 'chinese'
a,b,c = string[0],string[1],string[2:]
print(a,b,c)
string = 'chinese'
a,b,c = (string[0],string[1],string[2:])
print(a,b,c)

[a,b,c] = '123'
print(a,b,c)
a,*b = 'chinese'
print(a,b)

a,b,*c = 'cs'
print(a,b,c)

for (a,*b,c) in [(1,2,3,4),(5,6,7,8)]:
    print(a,b,c)
    a,*b,c = (1,2,3,4,5,6)

print(a,b,c)

for all in [(1,2,3,4),(5,6,7,8)]:

    a,b,c = all[0],all[1:3],all[3]

    print(a,b,c)
    a=b=c='chinese'
print(a,b,c)

a=b=0
b=b+1
print(a,b)
L = [1,2]
print(L.append(3))
print(L)
print(a,b,c)
print(a,b,c,sep='$')
print(a,b,c,sep='&',end='\r\n')
print(a,b,c,sep='*')
print(a,b,c)
print(a,b,c,sep='*')
print(a,b,c,end='')
print(a,b,c)
a,b,c = (1,2,3)


print(a,b,c,sep='%',end='',file=open("demo52.txt","w"))
print(dir(sys))
import sys

sys.stdout.write("hi");
sys.stdout = open("demo52_1.txt","a")

a,b,c = ('a','b','c')

print(a,b,c)
sys.stdout = open("demo52_2.txt","a")  #当前标准输出流是一个文件
a,b,c ='123'
print(a,b,c)  #打印的内容以默认的sep,end值输入到默认指定的标准输出流
print('hello')

sys.stdout.close()  #关闭当前标准的默认输出流

print('back here')  #由于输出流关闭导致无法输出
"""

import sys
temp = sys.stdout #默认的标准输出流
sys.stdout = open("demo52_3.txt",'a')  #指定的标准输出流
print("spam")
print("123")

sys.stdout.close()

sys.stdout = temp

print("back here")