import time
import calendar
import math

""""
print(time.time())
print(help(calendar.month))
print(calendar.month('2018','01'))
print("the math of pi is:{0:.3f}".format(math.pi))

print("there are some {name},which weight is {0:.2f}".format(math.pi,name='egges'))

table = {'name':'tony','age':'100','address':'shanghai'}

print(table)

for k,v in table.items():
    print("{0:10}--{1:10}".format(k,v))
vegetable = {'apple':'100','bannana':'200','fruit':'324'}

for k,v in vegetable.items():
    print("{0:10}----{1:10d}".format(k,v))
    
print("there are %5.3f" % math.pi)
print("there are %s" % math.pi)
f = open("baidu1.html")

print(f)
print(type(f))
print(f.read())
#f.close()
#print(f.read())
#print(f.read(10))

print(f.readline())
print(f.readline())
print(f.readline())
f = open("demo23.txt",mode="r")

for line in f:
    print(line,end='')
f.close()
s = (
    ('tony','jack','tom'),
    ('23','34',56)
)

f.write(str(s))
s = {
    'name':'tom',
    'age':'100',
    'address':'beijing'
};

f.write(str(s))
s = ['jack','tom','tony','junly']

f.write(repr(s))
s = {
    "job":['php','python','javascript','java'],
    "age":"100",
    "friends":{
        "tony":"100",
        "jack":"20",
        "shui":"29"
    },
    "house":("beijing","shanghai","korea","japanese")
}


f.write(repr(s))
#print(f.readline())
print(f.read(1))

print(f.tell())

f.seek(5)

print(f.read())

print(f.tell())
f = open("demo33.3.txt",mode="rb")


with

f.close()
with open("demo33.2.txt") as f:
    read_data = f.read()
    print(read_data)

"""




