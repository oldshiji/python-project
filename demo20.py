import time

""""
def showmsg(title,content,*attribute,**job):
    print(title)
    print(content)
    print(attribute)
    print(job)



showmsg('Alert','warning','there are some alert',key1='val1',key2='val2')

def alert(title,content='Do u want to delete this record?',type='prompt'):
    if type == 'prompt':
        print(title)
        print(content)
    elif type == 'info':
        print(title,content)




#alert('ASK')
#alert('Info',content='Fatal warning!',type='info')
#alert(content='there are some body will trick u if u treason',type='prompt',title='warning')
alert(content='accord ours conference,will have some argue between ours meeting',type='prompt','msg')
def write_multi_content(file,separator,*con):
    file.write(separator.join(con))



f = open("demo20.txt",mode='w',encoding='utf8')

write_multi_content(f,'/','accord your sistuation we will sketch some argument')
f = open("demo20.txt",mode='r')
con = f.read()
print(con)
print(list(range(3,6)))
args = [3,6]

print(range(*args))
print(list(range(*args)))

def showinfo(title,**info):
    print(title)
    print(info)


info = {'name':'tony','age':'100','height':'190','address':'beijing'}

#showinfo('someinfo',info)
showinfo('someinfo',**info)
def showmsg(a,b):
    return lambda a,b:a/b



f = showmsg(10,100)

print(f)
print(f(10,20))

info = 'there are some milk'
f = lambda info:info
print(f)
print(f(info))
print(data)
print(list(data))
print(sorted(data))
print(i[0])
    print(i[1])
    print(i[2])
    print(len(i))
    data = (
    ('tony','28','bejing'),
    ('jack','1000','shanghai'),
    ('tom','800','tianjing')
    data = (
    (1,2,3),
    (4,5,6),
    (7,8,9)
)


for i in data:
    #k = lambda i:i[0]+i[1]+i[2]
    #k = lambda i:sum(i)
    #print(k(i))
    #print(sum(i))
    k = lambda i:if sum(i)/2:i
    print(k)
)
def weigth(num:int)->'weight sum':
    print(weigth.__annotations__)
    print(num)

weigth(100)
"""

def showmsg(title:str='标题',content:str='内容')->'返回一条记录':
    print(title)
    print(content)
    print(showmsg.__annotations__)



showmsg('info','some stantard accordance')