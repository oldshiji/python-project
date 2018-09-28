

import os

""""shell = os.popen("date")

for line in shell:
    print(line)


for line in open("demo59.txt"):
    print(line)
num = [1,2,3,4,5]

for x in num:
    print(x)
    
num = 'abcde'

i = iter(num)

print(next(i))
print(next(i))

letter = 'chinese'
i = enumerate(letter)
print(i)

for x in i:
    print(x)

print(open("demo59.txt").readlines())
print([line.rstrip() for line in open("demo59.txt")])
print([line.upper() for line in open("demo59.txt")])

print([line.rstrip() for line in open("demo59.txt")])

print([line.rstrip().upper() for line in open("demo59.txt")])

print([line.replace('\n','&') for line in open("demo59.txt")])

print([('h' in line) for line in open("demo59.txt")])
print([line.rstrip() for line in open("demo59.txt") if line[0] == 'h'])
s = '2018/04/03  12:33    <DIR>          Windows10Upgrade'

print(s.find('Windows10Upgrade'))

//////////////////////////////
迭代器相关
    可迭代对象
        字符串
        列表
        字典
        元组
        集合
        文件资源
        shell命令资源
    迭代工具[函数]
        zip
        map
        filter
        functiontools.reduce
        iter
        enumiteraotr
    迭代结果为列表
        list函数处理
    迭代内置函数
    next __next__
    迭代协议
        迭代器的基本规则是可以迭代的对象支持从左到右方式扫描，内置指针从左向右移动

print(sum([1,2,3,4,5]))
#该函数使用了迭代协议　　它会依次循环计算

print(max([1,2,3,4,5]))
#依次循环判断最大值

print(min([1,2,3,4,5]))
#依次循环判断最小值

print(any(['a','','b']))
#依次循环判断只要有一个值为真时就为真

print(all(['a','','b']))
#依次循环判断所有的值为真时为值
print(open("demo59.txt").readlines())
print(list(open("demo59.txt")))
#打开文件，依次循环读取每一行　以列表形式输出

print(tuple(open("demo59.txt")))
#打开文件，依次循环读取每一行，以元组形式输出

print('&&'.join(open("demo59.txt")))
#打开文件，依次循环读取每一行，并以&&符号连接

a,b,c = open("demo59.txt")
#打开文件，依次循环读取每一行，并将每行单独赋值给左边的变量
print(a,b,c)


a,*b = open("demo59.txt")
#打开文件，依次循环读取第一行，并将第一行赋值给变量a，剩余的数据全部赋值给左边的列表变量b

print(a,b)
print(set(open("demo59.txt")))
#打开文件，依次循环读取每一行，以集合形式输出
print({line for line in open("demo59.txt")})
print({lx:line for lx,line in enumerate(open("demo59.txt"))})
print([line for line in open("demo59.txt")])
迭代对象：文件资源
迭代语句：for语句
迭代函数：
迭代结果：列表
print({line for line in open("demo59.txt")})
迭代对象：文件资源
迭代语句：for语句
迭代函数：
迭代结果：集合
print(tuple(open("demo59.txt")))
print({k:v for k,v in zip(['name','age','address'],['刘德',27,'蜀国'])})
迭代对象：列表
迭代函数：zip
迭代语句：for语句
迭代结果：字典
迭代协议：zip函数将２个列表从左至右依次循环每一荐得到２个列表的每一项并将值赋值给变量k,v最后以字典形式输出

print([line for line in 'chinese'])
print([line for line in 'chinese' if line =='e'])
print([(a,b) for a in 'chinese' for b in 'japanese'])
print(open("demo59.txt").readlines())

print([line.rstrip() for line in open("demo59.txt")])
print(set(open("demo59.txt")))

print(f(1,2,3,4))


print(f(*[1,2,3,4]))
print({lx:line for (lx,line) in enumerate(open("demo59.txt"))})
def f(a,b,c):
    print(a,b,c,sep='&')



#print(f(*open("demo59.txt")))

print(f(open("demo59.txt")))
l1 = [1,2,3]
l2 = ['a','b','c']

print([line for line in list(zip(l1,l2))])

print([line for line in map(ord,l2)])
print(R1)

print(next(R1))

r1 = iter(R1)
print(next(r1))
print(next(r1))
R1 = range(3)

r1 = iter(R1)
r2 = iter(R1)

print(next(r1),next(r2))
print(next(r2))
print(next(r1))
r1 = zip([1,2,3],['a','b','c'])
print(next(r1))
print(next(r1))

r2 = iter(r1)
print(next(r2))
print(next(r2))
m1 = map(ord,['a','b','c'])
print(m1)
print(next(m1))
print(next(m1))

m2 = iter(m1)
print(next(m2))
print(next(m2))
f1 = filter(bool,['a','b','c'])
print(next(f1))
print(next(f1))

f2 = iter(f1)
print(next(f2))
e1 = enumerate('chinese')
print(e1)
print(next(e1))

print(list(e1))
print(k)
print(next(k))
print(d)

k = d.keys()

print(list(k))

v = d.values()
print(list(v))
d = dict(a=1,b=2,c=3)

print(d.items())
for k,v in d.items():
    print(k,v,sep='=')
    
d = dict(zip(['a','b','c'],[1,2,3]))
print(d)

i = iter(d)
print(next(i))
print(next(i))
"""


d = dict(a=1,c=3,b=2)
print(d)

print(d.keys())
print(sorted(d.keys()))

for k in sorted(d.keys()):
    print(k,d[k],sep='=')


for k in sorted(d):
    print(k,d[k],sep='&')