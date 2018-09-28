import time
import random
import calendar
import sys
""""

print(time.strftime('%Y-%m-%d',time.localtime(time.time())))
print(random.random())
print(random.randint(20,80))
print(random.randrange(1,100))
print(random.choice([1,2,3,4,5]))


#print(help(calendar.month))
print(calendar.month(theyear=2018,themonth=2))

conjunction = "dead"

bird = "this is %d %s birds" % (1,conjunction)

print("there are %d %s in this garden" % (100,'trees'))
print(bird)
print("last night there are %d %s were arrested by local policemen" % (20,['treason','royal','temple','communisum']))

#%[name][flags][width][precision] typecode
x = 1234

res = "integers:%d---%-6d---%06d---%+8d" % (x,x,x,x)

print(res)
x = 1.23456789

print("%e--%f--%g--%E" % (x,x,x,x))
print("%f--%.2f--%.*f"%(1/3.0,1/3.0,6,1/3.0))
print("there are %(name)s in the %(age)d" % {'name':'fisherman','age':100})
#%u,%s,%c,%d,%f,%e,%g,%o,%E


replay = 
    Hello,%(name)s,
    Welcome to back
    Your age is %(age)d


person = {'name':'jack','age':300}

print(replay % person)


food = "fish"
weight = 30

print("we will supply %(food)s in %(weight)d" % vars())
template = "{0},{1},{2}"

print(template.format("japanese","america","korea"))
template = "{j}--{a}--{k}"

print(template.format(j='japanese',a='america',k='korea'))

template = "ther are {0} countrys which are {j},{a},{k} in different place"

print(template.format(3,j='japanese',a='america',k='korea'))

template = "tony age is {0},his jobs are {job}"

print(template.format(100,job=['phper','python','vhdl']))

template = "{motto},{0} and {food}".format('spam',motto='discourage',food=['fish','big','chicken'])

x = template.split("and")

print(x)

y = template.replace("and","和")

print(y)


template = 'My {1[spam]} runs {0.platform}'.format(sys,{'spam':'desktop'})

print(template)
template = 'My {config[spam]} runs {sys.platform}'.format(sys=sys,config={'spam':'desktop'})
print(template)

print("first={0[0]},second={0[1]}".format(somelist))

print("fisrt={0},second={1}".format(somelist[0],somelist[1]))
somelist = list('CHINESE')

#字符串以逗号分隔得到提元组对象
part = somelist[0],somelist[-1],somelist[1:3]

print(part)

print("first={0},middle={2},last={1}".format(*part))
"""

somelist = list("CHINESE")

part = {'first':somelist[0],'second':somelist[1],'last':somelist[-1]}

print("first={config[first]},second={0[second]},last={config[last]}".format(part,config=part))
