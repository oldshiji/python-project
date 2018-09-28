
""""
x = 99

def add(y):
    z = x+y
    return z



print(add(1))
print(x)
print(z)
import builtins

print(dir(builtins))

def hider():
    open = 'spam'  #本地作用域　　定义了此变量则会覆盖内置变量open函数　　open是函数名　但python称之为变量　本身是存储一个函数对象
    open("http://www.baidu.com")

x = 99

def add():
    x = 99



add()

print(x)
hider()
def func():
    global x
    x = 99


func()

print(x)
#工厂函数
def maker(n):

    def action(x):
        return x*n
    return action


f = maker(10)
print(f)

print(f(20))

g = maker(3)
print(g(3))
def func():
    x = 4
    action = (lambda n:n**x)
    return action


f = func()

print(f(5))
x = 99 #全局变量　　作用域为整个模块　　模块作用域
def func(y):#全局函数名　　作用域为模块作用域
    z = y+x #局部变量　　作用于该函数中
    return z



print(func(10))

#zip是个函数名并指向了该函数对象
#作用域为内置__builtin__里
print(zip([1,2,3]))
import builtins

print(builtins.zip([1,2,3,4,5]))
def hider():
    open = 'spam' #本地作用域的变量覆盖掉了全局变量函数open　　导致由函数变成了字符串

    open("http://www.baidu.com")



hider()
x,y=10,20
def func():
    global z
    z=x+y
    print(z)



func()
var = 99
def local():
    var = 0

def global1():
    global var
    var+=1


def global2():
    var = 0
    import thismod
    thismod.var+=1

def global3():
    var = 0
    import sys
    glob = sys.modules['thismod']
    glob.var+=1



def test():
    print(var)
    local();global1();global2();global3();
    print(var)


test()
var = 0

def globals():
    var = 0


def globals1():
    global var
    var+=1


def globals2():
    import demo65
    demo64.var+=1



def test():
    globals()
    globals1()
    globals2()

    print(var)


test()
全局作用域[块作用域]
此作用域下有x,f1全局变量　x为普通变量　f1为函数变量

局部作用域[函数作用域]
f1内嵌了一个临时函数[形成了嵌套作用域]　　类似闭包
在此作用域下有x,f2为嵌套作用域变量

根据LEGB[local enclosing function global builtings]
f2函数找到了x局部变量
x = 99

def f1():
    x = 88
    def f2():
        print(x)

    f2()


f1()
模块作用域下有x f1两个全局变量
f1下有x,f2嵌套的变量
f1函数内执行了返回f2函数对象变量
但它的作用域仍然是在f1之下，也就是f2绑定了f1作用域
x = 99

def f1():
    x = 88
    def f2():
        print(x)

    return f2


action = f1()

action()

def maker(x):
    def action(n):
        return x**n

    return action



f = maker(2)
print(f)
print(f(2))
def func(x):

    action = (lambda n:x**n)
    return action


f = func(4)

print(f)
print(f(2))
def func():
    acts = []
    for i in range(5):
        acts.append(lambda x:i**x)

    return acts


f = func()

print(f)
print(f[0])
print(f[0](2))
def func():
    acts = []
    for i in range(5):
        acts.append(lambda x,i=i:i**x)


    return acts



f = func()
print(f[0])

print(f[0](2))
print(f[1](2))
print(f[2](2))
print(f[3](2))
def tester(start):
    state = start
    def nested(label):
        print(label,state)

    return nested


F = tester(0)
print(F)
print(F('spam'))
模块作用域下有
tester函数变量

tester函数作用域下有
state,start,nested变量

nested函数作用域有
lable
在此作用域下能访问上层作用域的变量，但无法修改操作
def tester(start):
    state = start
    def nested(label):
        print(label,state)
        state+=1

    return nested

F = tester(0)
print(F)
print(F('spam'))

def teser(start):
    state = start
    def nested(label):
        nonlocal state
        print(label,state)
        state+=1

    return nested

F = teser(0)
print(F)
print(F('spam'))

F = teser(1)
print(F)
print(F('spam'))
"""

class A():
    def listen(self,port):
        print(port)


    def show(self):
        print("hello,world")

class B(A):
    def __init__(self):
        self.listen(80000)



#b = B()
B().show()