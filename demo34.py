import redis
import math
import random
#from decimal import Decimal
import decimal
from fractions import Fraction
""""
r = redis.StrictRedis(host='localhost',port='6379',db=1,charset='utf8')


print(r.keys("*"))
print(r.ping())
print(r.echo('hello,world'))

print(type(r.time()))
a = 3
b = 4
a,b=b,a

print(a,b)
print(a+b,a-b,a/b,a*b,a**b,a%b,a//b,a|b,a&b,a^b)
a = 0o123
b = 0xff
c = 0b10001111

print(a,b,c)

print(bin(c),oct(a),hex(b))

print(bin(i))
print(bin(j))

print(i|j,i&j,i^j)  #或　　与　　异或　　

0000 0001
0000 0010
-------------
0000 0011 = 3  #或操作　规则0|0=0 0|1=1 1|1=1

0000 0001
0000 0010
-------------
0000 0000 = 0 #与操作　　规则0&0=0 1&1=1 0&1=0

0000 0001
0000 0010
--------------
0000 0011 3   #异或　　规则　　0^0=0 1^1=0 1^0=1 0^1=0
print(bin(i<<2))  #i左移２位为４

data = [
    '0x01',
    '0x02',
    '0x03',
    '0x04',
    '0x05',
    '0x05',
    '0x06',
    '0x07',
    '0x08',
    '0x09',
    '0x0a',
    '0x0b',
    '0x0c',
    '0x0d',
    '0x0e',
    '0x0f',
    '0x10',
    '0x11',
    '0x12',
    '0x13',
    '0x14',
    '0x15',
    '0x16',
    '0x17',
    '0x18',
    '0x19',
    '0x1a',
    '0x1b',
    '0x1c',
    '0x1d',
    '0x1e',
    '0x1f',
    '0x20'
]

#print(data)

for i in data:
    print(int(i,10))
    
i = 0b00000001  #0000 0001
j = 0b00000010  #0000 0010


print(i+j)
print(9**99999999)
print('{0:b},{1:o},{2:x}'.format(64,64,64))
i = 8

print(bin(i))
print(bin(i<<2),bin(i>>2),bin(i|1),bin(i&1),bin(i^1),bin(i))
i = 256
print(bin(i),i.bit_length())

print(len(bin(i)))
print(math.pi,math.e,pow(3,3),math.sqrt(144))
print(max(1,2,3),min(1,2,3),sum(1))
print(sum(1,2,3,4,5))
print(math.floor(2.567),math.floor(-2.567)) # 向下取整
print(math.trunc(2.567),math.trunc(-2.567))　#取整

print(round(2.567),round(-2.567))　#正数向上取整数，负数向下取整

print(round(2.567,2),round(-2.567,2))

print("{0:.1f}".format(2.567),"{0:.2f}".format(-2.567))

print(1/3,round(1/3,2),"{0:.2f}".format(1/3))
print(math.sqrt(144)) #计算平方根  模块
print(144**.5)　　#表达式
print(pow(144,.5))　　#函数
print(random.random())
print(random.randint(1,10),random.randint(20,100))
print(random.choice(['a','b','c','d']))
print(0.1+0.1+0.1-0.3)  #浮点数运算不准确
print(0.1+0.1+0.1)

print(round(0.1+0.1+0.1,1)-0.3)
print(0.1+0.1+0.1-0.3)
print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3'))
print(Decimal(1)/Decimal(7))
print(decimal.Decimal(1)/decimal.Decimal(7))

decimal.getcontext().prec=4

print(decimal.Decimal(1)/decimal.Decimal(7))
print(Fraction(1,3))
print(Fraction(2,3))
print(Fraction(4,6))
x = Fraction(1,3)  # 分数　　３分之１
y = Fraction(4,6)

print(x,y)
print(x+y,x-y,x*y)
print(Fraction('.25'))
print(Fraction('1.25'))

print(Fraction('.25')+Fraction('1.25'))
x = Fraction(1,10)
y = Fraction(1,10)
z = Fraction(1,10)

r = Fraction(3,10)

print(x+y+z-r)

print(decimal.Decimal('0.1')+decimal.Decimal('0.1')+decimal.Decimal('0.1')-decimal.Decimal('0.3'))
x = 2.5
print(x)
print(x.as_integer_ratio())

print(Fraction(*x.as_integer_ratio()))
print(Fraction(1,3))
print(Fraction('0.3'))
print(Fraction(*1.3.as_integer_ratio()))
print(Fraction.from_float(1.75))
print(Fraction(1,3))
print(Fraction('0.03'))
x = 1.3
print(Fraction(*x.as_integer_ratio()))
print(Fraction.from_float(0.03))
x = 5.5
print(x)
print(x.as_integer_ratio())
print(Fraction(*x.as_integer_ratio()))
print(Fraction.from_float(5.5))
print(Fraction(11,2))
print(Fraction('5.5'))

print(1/3)
print((1/3).as_integer_ratio())
print(x,y)

for i in x:
    print(i)


for i in y:
    print(i)


print(len(y))

x = set('abcde')
y = set('1234567890')
x = set("abcde")
y = set("bdxyz")

print(x-y)
print(x|y)
print(x&y)

print(x^y)
print(x-y)  #差集
print(x|y)  #并集
print(x&y) #交集

print(x^y) #异或集
abcd
abde
-------
00ce
x = set("abcd")
y = set("abde")


print('a' in x)
print(x<y)

z = x.intersection(y)  #交集处理
print(z)

print(x.add("china"))  #向集合添加项
print(x)

print(x.update(set(['japanese','america'])))  #修改集合

print(x)
x = set("abc")
y = set("abd")
print(x)

x.update(set(['china','gov','communism','conference','prefenence','fond']))

print(x)

x.remove("china")
print(x)
s = set([1,2,3])
print(s)

print(s|set([3,4,2]))
print(s.union(set([5,4,3])))

print(s.intersection(set([1,2])))

print(s.issubset(set([1,2,3,4,5,6])))
#print(x,y)
print(x-y)
print(x|y)
print(x&y)
print(x.union(y))
print(x.intersection(y))
print(x.add('china'))
print(x)
x = {'a','b','c','d'}
y = {'a','b','c','e'}


x.update({'china','japanese'})
print(x)

x.remove('japanese')

x = {} #字典
y = set()#集合

print(type(x),type(y))

print({1,2,3}-{2,3,4})

print({1,2,3}|{2,3,4})

print({1,2,3}&{2,3,4})

print({1,2,3}^{2,3,4})

print({1,2,3}.union({2,3,4}))
print({1,2,3}.intersection({2,3,4}))
print({1,2,3}.issubset({2,3,4}))
"""

x = {1,2,3,4,5}
#x.add(['a','b'])
#x.add({'a':'b'})
x.add(("a","b"))

print(x)