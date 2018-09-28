import time
import calendar
import sys
import os

""""
print(calendar.month(theyear=2018,themonth=4))

print(time.strftime('%Y-%m-%d',time.localtime(time.time())))
a,b = 1,20

while a:

    if a==5:
        continue
    elif a==10:
        break
    else:
        print(a)

    a+=1
else:
    print('finish')
    a = 10

while a:
    a-=1

    if a%2==0:continue  # 2 4 6 8 10
    print(a)
    a = 10
while a:
    a-=1
    if a%2==0:
        print(a)
        
while True:
    name = input("Enter your name:")
    if name=='stop':break
    age = input("Enter your age:")

    print("hello",name,'your age is ',int(age)**3)
"""


print("Welcome to use py command line",time.strftime('%Y-%m-%d',time.localtime(time.time())))
print(os.name,os.path)
while True:
    action = input("root@localhost#:")
    controller = {
        'init':'命令初始化',
        'cal':calendar.month(theyear=2018,themonth=3),

        'help':'功能完善中'
    }
    if action in controller:
        print(controller[action])
