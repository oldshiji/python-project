import sys
"""
while True:
    a = input()
    #print(a**2)
    #print(int(a)**2)
    #startRun = run
    #startRun(a)
    #print(startRun.name)
    #print(startRun.showname())
    print(times(a,3))



def run(str):
    a = {
        'a':'your str is a',
        'b':'your str is b',
        'c':'your str is c',
        'd':'your str is d'
    }

    if str in a:
        print(a[str])
    else:
        print('你输入的东西不存在')

run.name = '这是一个根据命令返回不同数据的函数'


def showname():
    print("我是一个函数哦")



run.showname = showname

def times(a,b):
    return a*b


"""

def intersect(set1,set2):
    a = list()
    for x in set1:
        if x in set2:
            a.append(x)

    return a


a,b = 'chinese','japanse'

print(intersect(a,b))

print([x for x in a if x in b])

print(intersect(['a','b','c'],('a','e')))