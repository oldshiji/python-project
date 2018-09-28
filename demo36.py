import math
import decimal
import random
from fractions import Fraction
import sys

""""
print(math.pi)
print(decimal.Decimal('0.0002'))
print(random.random())
print(random.randint(1,10))
print(random.choice(['a','b','c']))
print(Fraction(1,2))
x = 0.5
print(Fraction(*x.as_integer_ratio()))
print(Fraction('0.5'))
print(Fraction(Fraction.from_float(0.5)))

print(x)
print(bin(x))
print(bin(x<<3))
print(x.bit_length())
print(x+y)
print(x-y)
print(x*y)
print(x/y)

print(x|y)
print(x&y)
print(x^y)
x = 0b00000001
y = 0b00000010


print(len(x))
a = set("abcdefh")
b = {'a','b','c','d'}

print(a,b)
print(a-b)
print(a|b)
print(a&b)
print(a.union(b))
print(a.intersection(b))


print(a.add('5'))
print(a)

a.update([4,5,6])
print(a)
a = set([1,2,3])
b = set([2,3,4])

for i in a:
    print(i)
    print({x**2 for x in [1,2,3,4,5]})
print({x*2 for x in 'chinese'})
print([x*2 for x in [1,2,3]])
print({x*2 for x in set([1,2,3])})
print({x*2 for x in {'a','b','c'}})
print({x*2 for x in (1,2,3)})

print([x*2 for x in [1,2,3]])
print([x*2 for x in {'a','b','c'}])
print([x*2 for x in set([1,2,3])])
print([x*2 for x in (1,2,3,4)])
print([x*2 for x in 'japanese'])

l = [1,2,3,4,5]
print(l)

print(set(l))

print(list(set(l)))
enginerrs = {'张飞','刘备','曹操'}
managers = {'张飞','刘备','吕布'}

print('张飞' in enginerrs)  #张飞是工程师吗
print(enginerrs&managers) #查找是工程师又是管理员的人员
print(enginerrs|managers)  #将工程师和管理员组合
print(enginerrs-managers) #从工程师查找哪些人不是管理员
print(managers-enginerrs) #从管理员查找哪些人不是工程师
print(enginerrs>managers)
print({'张飞','刘备'} < enginerrs)  #查找这２个人是否是工程师
print({'张飞','刘备','曹操'} > enginerrs)
print(enginerrs^managers) #异或处理　　查找既不是工程师和管理员的人员  要求条件

print(False,True)
print(True+4)
print(True | False)
print(isinstance(True,int))
print(True is 1)
print(False is 0)
print(True==1)
print(False==0)
a = 3

print(a)
print(type(a))
print(a.bit_length())
print(a.__eq__(3))

print(3.bit_length())
print(3.__eq__(3))
l = [2,3,4]  #l变量保存了list列表类型对象的引用[指针地址]　　该变量保存的一个指向[2,3,4]这个列表类型对象的地址
print(l)
print(type(l))  #获取该变量存储的指针引用的数据类型
print(isinstance(l,list)) #判断此变量保存的引用地址数据类型是否是list类型对象
l1 = l  #将l变量保存的引用地址赋值给l1  此时l1和l都同样指向[2,3,4]列表对象
l[0] = 20　　
print(l)
print(l1)

l1=l ------>[2,3,4]
变量　　　引用　　　对象

l1  = [2,3,4]  #此处变量l1　　保存了[2,3,4]的指针地址即引用

l2 = l1[:]　　#l2保存了l1通过分片copy的数据，重新开辟了新的内存空间
l1[0] = 20

print(l1,l2)
L = [1,2,3]  #变量L保存了[1,2,3]的指针地址
M = L　　#变量M和L同时指向[1,2,3]的引用

print(M==L)　　#比较２个变量的值是否相等
print(M is L)　#比较２个变量保存的引用是否相同，意即是否同时指向一个同一个引用地址
L = [1,2,3]
M = [1,2,3]
#以上２个列表值相等，但变量之间保存的引用地址不一样
print(L==M)
print(L is M)
print(sys.getrefcount(1))

print(sys.getrefcount('a'))
L = [1,2,3]  #引用一次
M = L　　#引用２次
H = M　　#引用３次
I = H　　#引用４次

print(sys.getrefcount(L))  #引用5次
a = 'chinese'
b = a
b = 'japanese'
a = 'chinese"'
b = "japanese'"
c = '''america'''
d = indian

e = "s\ttd\n"
f = r"c:/test.txt"
g = b'sp\0x1am'

print(a,b,c,d,e,f,g)
print(a,b)
"""

print("hello",'world')
print("hell'0",'worl"d')

print("hello" 'jack',"tom")
