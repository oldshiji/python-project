import time

""""
a = 'conjunection'

for x in a:
    print(x)
    a = ['a','b','c','d']

for x in a:
    print(x)
a = {'a':1,'b':2}

for x in a:
    print(x,a[x])

a = {'a':'jack','b':'tony'}

for x in a.items():

    k,v = x
    print(k,v)
    
for (a,*b,c) in [(1,2,3,4),(5,6,7,8)]:
    print(a,b,c)
for all in [(1,2,3,4),(5,6,7,8)]:
    a,*b,c = all[0],all[1:3],all[3]
    print(a,b,c)
    for key in tests:
    for k in items:
        if key==k:
            print(key,'was found')
            break
    else:
        print('not found')
        items = ['aaa',(4,5),'aaabb']
tests = [(4,5),3.14]

for key in items:
    if key in tests:
        print(key,'was found')
else:
        print('not found')
        set1 = set('chinese')
set2 = set('japanese')
print(set1.intersection(set2))

print(set1.union(set2))

print(set1.difference(set2))
print('----------------------------')
print(set1-set2)
print(set1+set2)
a = 'spam'
b = 'scam'
c = []
for x in a:
    if x in b:
     c.append(x)



print(c)

file = open("demo52_2.txt","r")
print(file.read())

print("-------------------------------")

while True:

    line = open("demo52_2.txt","r")
    if not line:
        print(line.readline())
        file = open("demo52_2.txt","r")


while True:

    line = file.readline()
    if not line:break
    print(line)
    import sys
for line in open("demo52_2.txt","r"):
    if not line:break
    print(line)


print("-------------------")

for line in open("demo52_2.txt","r").readline():
    if not line:break
    print(line,sep='-',end='\n',file=sys.stdout)
    print(list(range(5)),list(range(2,5)),list(range(0,10,2)))

a,b,c = range(5),range(2,5),range(0,10,2)
print(list(range('a','z')))
print(a,b,c)
import random

print(random.choice(['a','z']))
for x in range(3):
    print(x,'pythons')
    x = 'spam'
for a in x:
    print(a)
    a = 'spam'
for x in range(len(a)):
    print(x,a[x])
    
print(list(range(0,len(a),2)))

for x in list(range(0,len(a),2)):
    print(a[x],a[x].upper())
"""


a = "abcdefghigklmnopqrstuvwxya"
#字符串，列表，元组均支持索引，分片操作
#默认的分片操作是３个参数
#start,end,step 起始值，终止值　　步进值
#a[::2]  表示从０到len(a)最后一个，并且以步进２开始
for x in a[::2]:
    print(x,x.upper())