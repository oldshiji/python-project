import calendar

""""
print(calendar.month(theyear=2018,themonth=2))

if (x<y){

    x = 1
    y = 2
}

other language fromat of if 

x,y = 10,20
if x<y:
    x = 1
    y = 2





print(x,y)
while True:
    replay = input("请您输入字符:")
    if replay == 'stop':break
    print(replay.upper())
    a = '20'
print(int(a)**2)

while True:
    replay = input("请输入要求平方的数字:")
    if replay == 'stop':break
    if replay.isnumeric():
        print(int(replay)**2)
    else:
        print("您输入的不是数字")


print("Bye")
a = 'c'
a.isdigit()
while True:
    replay = input("请输入数据：")

    if replay=='stop':
        break
    elif not replay.isdigit():
        print("Bad!"*8)
    else:
        print(int(replay)**2)


print("Bye")
while True:
    replay = input("请输入数据：")
    if replay=='stop':break
    try:
        replay = int(replay)
    except:
        print("Bad!"*8)
    else:
        print(int(replay)**2)

print("Bye")
while True:
    replay = input("请输入数据：")
    if replay=='stop':
        break;
    elif not replay.isdigit():
        print("Bad!"*8)
    else:
        if int(replay)<20:
            print("low")
        else:
            print(int(replay)**2)


print("Bye")
a = "chinese"
print(a)

a,b = 'chinese','japanese'
print(a,b)
[a,b] = ['chinese','japanese']
print(a,b)
a,b,c,d = 'abcd'
print(a,b,c,d)
a,*b='chinese'
print(b)
a=b='chinese'
print(a,b)

a=10
a+=80
print(a)

[a,b,c] = ('a','b','c')
print(a,b,c)
(a,b,c) = ['a','b','c']
print(a,b,c)
基本赋值
元组赋值
列表赋值
多目标赋值
增加赋值
序列赋值
(a,b,c) = 'abc'
print(a,b,c)
string ='spam'
a,b,c,d=string
print(a,b,c,d)

string ='spam'


a,b,c=string
print(a,b,c)
lang = 'chinese'
print(lang)
a,b='1','2'
print(a,b)

[a,b] = 1,2
print(a,b)
a,*b = 'chinese'
print(a,b)
a,b,c,d='1234'
print(a,b,c,d)
a = 9
a+=99
print(a)
(a,b,c) = ['a','b','c']
print(a,b,c)
[a,b,c,d,e,f,g] = 'chinese'

print(a,b,c)
a,b,c,d = string
print(a,b,c,d)

a,b,c = string
print(a,b,c)
a,b,c = string[0],string[1],string[2]
print(a,b,c)

a,b,c = list(string[:2])+[string[2:]]　#list函数用于创建列表　　string[:2]得到S,P两个字母，分别赋值给a,b,后面[string[2:]]也是一个列表
　　　　　　　　　　　　　　　　　　　　　　#整合合成一个列表结果是　　['S','P','AM'] 的元组方式赋值

print(a,b,c)
a,b = string[:2]
c = string[2:]

print(a,b,c)
(a,b),c = string[:2],string[2:] #(a,b)为一个元组，再和c组合成新的元组　　string[:2]将２个元素分别赋值，string[2:]赋值给c

print(a,b,c)
((a,b),c) = ('SP','AM')

print(a,b,c)
for (a,b,c) in [(1,2,3),(4,5,6)]:
    print(a,b,c)
    string = 'SPAM'  #赋值类型　　基本赋值


for ((a,b),c) in [((1,2),3),((4,5),6)]:
    print(a,b,c)
def f(tuples):

    ((a,b),c) = tuples

    print(a,b,c)




f(((1,2),3))

red,green,blue = range(3)

print(red,green,blue)
L = [1,2,3,4]

while L:

    front,l = L[0],L[1:]
    print(front,l)
    l = [1,2,3,4]

a,b,c,d = l
print(a,b,c,d)
a,b = 'seq'
print(a,b)
a,*b = 'seq'
print(a,b)

*a,b = 'seq'
print(a,b)
seq = [1,2,3,4]

a,*b,c = seq # a=1,b=[2,3] c = 4

print(a,b,c)
a,*b = 'chinese' # a='c' b='hinese'

print(a,b)

a,*b,c = 'chinese'

print(a,b,c) #a='c' b='hines' c='e'
a = 'chinese'

print(a[0],a[:5],a[6])

print(a[0],a[1],a[2:])
print(L[0],L[1:])
print(L[1],L[2:])
print(L[2],L[3:])
print(L[3],L[4:])

while L:
    front,*l = L
    print(front,l)
    
L = [1,2,3,4]

a,b,c,*d = L

print(a,b,c,d)
a,b,c,d,*e = L
print(a,b,c,d,e)
a,b,*e,c,d = L
print(a,b,c,d,e)
a,*b,c,*d = L
print(a,b,c,d)
*a = L
print(a)
*a, = L
print(a)
a,*b = L
print(a,b)
a,b = L[0],L[1:]
print(a,b)
*a,b = L
print(a,b)
"""


L = [1,2,3,4]


a,b = L[:-1],L[-1]

print(a,b)
