
class Manager():
    role = 'admininstrator'
    def __init__(self,name,age,sex):
        self.name = name
        self.age  = age
        self.sex  = sex
    def getName(self):
        print(self.name)
    def getAge(self):
        print(self.age)
    def getSex(self):
        print(self.sex)
    def create():
        print("create")
    def gets(self):
        print("gets")





'''
aa = 1000
def talk(param):
    print(param)
    return 666
import sys


method = getattr(sys.modules[__name__],'talk')
method(888)

print(getattr(sys.modules[__name__],'aa'))
import mokuai

method = getattr(mokuai,'talk')
method('888')
print(getattr(mokuai,'a'))

m = Manager('jack',20,'female')


def talk(param):
    print("hello,jack---%s"%(param))
setattr(m,'talk',talk)
m.talk('tom')

delattr(m,'talk')
print(m.talk('h'))
setattr(m,'money',1000)
print(m.money)
delattr(m,'money')
print(m.money)
def talk(param):
    print("hello,jack--%s"%param)


setattr(Manager,'talk',talk)
Manager.talk(Manager)
setattr(Manager,'talk',talk)
Manager.talk('ok')
setattr(Manager,'country','china')
print(Manager.country)
delattr(Manager,'country')
print(Manager.country)
setattr(Manager,'county','china')
print(Manager.county)
getName = getattr(Manager,'getName')
getName(m)
role = getattr(Manager,'role')
print(role)

gets = getattr(Manager,'gets')
gets(Manager)
getName = getattr(Manager,'create')
getName()
manager = Manager('jack',18,'male')
getName = getattr(manager,'getName')
getName()
getAget = getattr(manager,'getAge')
getAget()


name = getattr(manager,'name')
print(name)
role = getattr(manager,'role')
print(role)
defaultRole = getattr(manager,'role','defaultRole')
print(defaultRole)
import logging
defaultRole = getattr(manager,'role1','defaultRole1')

if defaultRole:
    print(defaultRole)
else:
    logging.warn("没有数据")
'''



