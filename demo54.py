import requests
import sys

a,b = 1,2
""""

print(a,b)
print(a,b,sep="*")
print(a,b,sep="*",end="")
print(a,b)

sys.stdout = open("demo54.txt","a")

print(a,b,sep="*")

print(a,b,sep="&",end="\n",file=open("demo54.txt","a"))
print(a,b,"这２个参数的输出已经定向输入到指定的文件里了")

*a, = 'chinese'
print(a)
print("请输入一个数字",sep="",end="\r\n",file=sys.stdout)

num = input()

while 1:

    print("当前的num值是:",num)
    num-=1




input()

sys.stdout.write("hello,world");

print(a,b)
sys.stdout.write(str(a)+' '+str(b)+'\n')
temp = sys.stdout
sys.stdout = open("demo54_1.txt","a")
print("hi")
print(a,b)

sys.stdout.close()

sys.stdout = temp

print("come back,here")
sys.stderr.write("Bad!"*8);

print("Bad!"*8,file=sys.stderr)
x,y = 10,20
print(x,y)
sys.stdout.write(str(x)+' '+str(y)+'\n')
print(a,b,file=open("demo54_2.txt","w"))
open("demo54_3.txt","w").write(str(a)+str(b))
print(open("demo54_3.txt","r").read())
if 1:
    print('true')
    
if not 1:
    print('true')
else:
    print('false')
    
num = input()
num = int(num)
if num==10:
    print('10')
elif num==20:
    print('20')
else:
    print('error')
    
#　模拟多路分支
choice = 'vegetable'

print({
    'apple':'5',
    'wheat':'6',
    'peach':'20',
    'vegetable':'2'
      }[choice])
      print({
    'apple':'5',
    'wheat':'6',
    'peach':'20',
    'vegetable':'2'
      }.get('peach','bad Choice'))
      fruit = {
    'apple':'5',
    'wheat':'6',
    'peach':'20',
    'vegetable':'2'
      }

choice = 'peach'
if choice in fruit:
    print(fruit[choice])
else:
    print('Bad choice')
    print(2<3,3<2)
    
or 逻辑或运算
真真为真
真假为假
假真为假
print(2 or 3,3 or 2)

print([] or 3)

print([] or {})

print(2 and 3,3 and 2) #１１为１

print([] and 3)　　　　#１０为０

print({} and [])　　　　#0 0为０
if x:
    a = y
else:
    a = z


print(a)
x,y,z = 1,2,3
a = 0

a=y if x else z

print(a)
a = 't' if 'a' else 'b'
print(a)

a = 't' if '' else 'b'

print(a)

while True:
    print('Press ctrl+c stop me')
    spam = 'chinese'

while spam:
    print(spam,end=' ')
    spam = spam[1:]
    a,b=0,10

while a<b:
    print(a,end=' ')
    a+=1
    a,b = 0,50

while a<b:
    print(a,end=' ')
    a+=1
    if a>=10:continue
    if a>=40:break
else:
    print('over')
    a,b = 0,10
while a<b:

    if a==5:continue
    print(a)
    a+=1
    a,b=0,10
while a<b:
    if a==5:break
    print(a)
    a+=1
    
while True:pass

def func1():
    pass

def func2():
    pass



func1()

func2()
def func1():
    ...


def func2():...



func1()

func2()
"""

x = ...

print(x)


