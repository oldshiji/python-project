import time
import calendar


""""
print(time.strftime('%Y-%m-%d',time.localtime(time.time())))

print(calendar.month(theyear=2018,themonth=2))

calendar_list = calendar.month(theyear=2018,themonth=2)

print(type(calendar_list))

for i in calendar_list:
    print(i)
    
template = "{0:10}--{1:10}".format('chinese','japanese')

print(template)
template = "{0:<10}---{1:>10}".format('chinese','japanese')

print(template)
template = "{0:e}--{1:.3e}--{2:g}".format(3.1415926,3.1415926,3.1415926)

print(template)
template = "{0:f}--{1:.3f}--{2:06.3f}".format(3.1415926,3.1415926,3.1415926)

print(template)
template = "{0:x}--{1:o}--{2:b}".format(255,255,255)

print(template)

print(help(list))

print(dir(list))
L = []
print(L)
L = [1,2,3,4]
print(L)
L = ['a','b','c',[1,2,3]]

print(L)
L = list('chinese')

print(L)

L = list(range(-4,4))

print(L)

print(L[0])
print(L[1])

print(L[0:3])

print(len(L))

print(L1,L2)


print(L1+L2)
L1 = [1,2,3]
L2 = ['a','b','c']
L3 = [4,5,6]


print(L1*5)
列表=[1,2,3,4,5]

print(列表)

for x in 列表:
    print(x)
    print(1 in L)
    print(L.append(6))

print(L)
print(L.extend([6,7,8]))
print(L)
print(L.insert(1,100))

print(L)
print(L.index(2))
print(L.count(2))
print(L.sort())
print(L)
print(L.reverse())
print(L)
del L[1]
print(L)
del L[1:2]
print(L.pop())

print(L)
print(L)

print(L.remove(4))

print(L)
L[1] = 200
print(L)
L[0:3] = [10,20,60]

print(L)
L = [1,2,6,3,4,5]

print([x**2 for x in L])
b = 'abcd'
c = ['a','b','c','d']

print({x*2 for x in a})
print([x*2 for x in a])

print({x*2 for x in b})
print([x*2 for x in b])

print({x*2 for x in c})
print([x*2 for x in c])
a = {'a','b','c'}

b = {'a','b','d'}


print(a-b)
print(a&b)
print(a.union(b))
print(a.intersection(b))
L = map(ord,'chinese')

print(list(L))
L = [1,2,3]

print(L+[4,5,6])
print(L*4)
a = [c*2 for c in 'chinese']
print(a)
b = []
for x in 'chinese':
    b.append(x)


print(b)
print(help(dict))
D = {}
print(type(D))
print(D)
D = {'name':'tony','age':200}

D = {'name':'tony','job':{'name':'phper'}}

print(D)

print(D)
D = dict.fromkeys(['a','b'])

print(D)
print(D['name'])
print('name' in D)


print(D.keys())
print(D.values())
print(D.items())

print(list(D.keys()))
print(list(D.values()))
print(list(D.items()))
D1 =D.copy()

print(D1)

D = dict(name='tony',age=100)


print(D.get('name'))

print(dict)
print(help(dict),dir(dict))

D = {}
print(D,type(D))
D = {'name':'jackma','job':{'merchant':'商人'}}

print(D)
D = dict.fromkeys(['a','b'])
D = dict(name='jackma',age=100)

print(D)

print(D['name'])
print('age' in D)
print(D.keys())
print(D.values())

print(D1.update(D2))

print(D1)
print(D1.pop('name'))
print(D1)
print(len(D2))

del D2['age']
print(D2)
D2['age'] = 300

print(D2)
D1 = {'name':'jackma'}
D2 = {'age':'200'}

print(D1.keys() & D2.keys())
a = {x:x*2 for x in range(10)}

print(a)
D = {}
print(D)
D = {'name':'jackma'}
print(D)
D = {'name':'jackma','job':{'merchant':'商人'}}
print(D)
D = dict(name='jackma')
print(D)
print(D)
D = dict.fromkeys(['a','b'])
D['a'] = 100
D['b'] = 200
print(D)
print(D)
D['a'] = 100
D['b'] = 200
print(D)
del D['a']

print(D)
D.pop('a')

print(D)
print(D['a'])
D.update({'name':'tom'})
print(D)
print(D.keys())
print(D.values())
print(list(D.keys()))
print(len(D))

print('a' in D)
print(D.items())
print(list(D.items()))

for x in list(D.items()):
    for j in x:
        print(j)
D = dict.fromkeys(['a','b'])
D['a'] = 100
D['b'] = 200
print(D.get('a'))
print(D.get('c'))
print(D.get('c',300))
table = {'php':'1995','python':'1989','c':'1969'}

for lang in table:
    print(lang,'\t',table[lang])
    
print(Martix)
print(Martix[(2,3,6)])
if (2,3,6) in Martix:
    print(Martix[(2,3,6)])
else:
    print(0)
    try:
    print(Martix[(2,3,6)])
except KeyError:
    print(0)
    
Martix = {}
Martix[(2,3,4)] = 88
Martix[(7,8,9)] = 99

print(Martix.get((2,3,6),0))
mel = {
    'name':'jack',
    'jobs':['phper','pyer','c'],
    'web':'http://www.baidu.com',
    'home':{'zip':'123456','state':'cd'}
}

print(mel)
print(mel['name'])
print(mel.get('name'))
print(mel['jobs'])
print(mel['jobs'][2])
print(mel['web'])
print(mel['home']['zip'])
#字典删除

D = dict.fromkeys(['a','b'],100,200)
print(D)
D = {}
D['name'] = 'tony'
D['age'] = 100
print(D)
print('name' in D)
print(D.get('name',10))
print(D.keys())
print(D.values())
print(D.pop('age'))
print(D.update({'address':'beijing'}))
print(D.items())
D = dict(name='tony',age=100)
print(D)
D = dict([('name','tony'),('age','100')])

print(D)
D = dict.fromkeys(['a','b'],0)

print(D)

D = list(zip(['a','b','c'],[1,2,3]))

print(D)
D = dict(zip(['a','b','c'],[1,2,3]))

print(D)
D = {k:v for (k,v) in zip(['a','b','c'],[1,2,3])}

print(D)
D = {x:x for x in [1,2,3,4]}

print(D)
D = {x:x*2 for x in 'chinese'}

print(D)
"""

D = {x[0].upper():x for x in ['chinese','japanese','america']}

print(D)





































