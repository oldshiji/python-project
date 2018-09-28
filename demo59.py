
""""
#
for x in [1,2,3,4,5]:
    print(x)

for x in ('a','b','c'):
    print(x,x.upper())

for x in 'chinese':
    print(x,x.upper())
f = open("demo59.txt","w")
f.write("hello\n")
f.write("world\n")
f.write("china")
print(f.read())

f.close()
for line in open("demo59.txt"):
    print(line)

print(iter(f) is f)
print(f.__next__())
print(f.__next__())
f = open("demo59.txt","r")
print(next(f))
print(next(f))
print(iter(s) is s)
print(next(s))
si = iter(s)
print(si)
print(next(si))
for x in s:
    print(x**2,end='')

s = [1,2,3,4]

I = iter(s)

while True:
    try:
        x = next(I)
    except StopIteration:
        break

    print(x)
D = {'a':1,'b':2,'c':3}

for k in D.keys():
    print(k,D[k])


d = iter(D)
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(os.popen("dir"))
dir = os.popen("dir")
print(dir.__next__())
print(dir.__next__())
print(dir.__next__())
print(dir.__next__())
print(dir.__next__())
print(dir.__next__())
print(dir.__next__())
print(dir.__next__())
print(dir.__next__())
print(dir.__next__())
print(dir.__next__())

import os


print(os.popen("time"))
L = [1,2,3,4,5]
for x in range(len(L)):
    L[x] += 10

print(L)

#
L = [1,2,3,4,5]

print([x+10 for x in L])
print(f.readlines())
f = open("demo59.txt","r")
line = f.readlines()
print([x.rstrip() for x in line])
"""


print([x.rstrip() for x in open("demo59.txt")])