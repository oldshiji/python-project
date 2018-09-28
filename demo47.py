import calendar

"""

print(calendar.month(theyear=2018,themonth=2))
t = 1,2,3

print(t)
t = (1,2,3,4,5)

print(t)
t = tuple('chinese')
print(t) 
print(t[0])

for x in t:
    print(x)
    print('c' in t)
    print(t.count('e'))
    print(t.index('i'))
    t = tuple('chinese')

t1 = (x for x in t)
print(t1)

f = open("demo47.xml","w",encoding='utf8')

f.write("<xml><user>张三</user><age>800</age></xml>")

f.close()
f = open("demo47.xml","r",encoding='utf8')

print(f.readline())
print(f.readline())

f.close()
print(open("demo47.xml","r",encoding='utf8').read())
for line in open("demo47.xml","r",encoding='utf8'):
    print(line)
    str1 = "there are {num}".format(num=100)

print(str1)
x,y,z=1,2,3
str1 = 'chinese'
D = {'a':1,'b':2}
L = [1,2,3,4,5]

f = open("demo47_1.xml","w")
f.write(str1+'\n')
f.write('%s--%s--%s\n'%(x,y,z))
f.write(str(L)+'$'+str(D)+'\n')
print(open("demo47_1.xml").read())
f.close()
print(type('str'))
a = 'chinese'

print(dir(a))

line = open("demo47_1.xml","r").readline()

print(line)

line = open("demo47_1.xml","r").readline()

print(line)

F = open("demo47_1.xml","r")

line = F.readline()
print(line)

line = F.readline()

print(line)
f = open("demo47_2.txt","w")
f.write("chinese\n")
f.write("%s,%s,%s\n"%(10,20,30))
f.write(str([1,2,3])+"$"+str({'a':1,'b':2})+"\n")

f.close()
F = open("demo47_2.txt","r")
line = F.readline()
print(line)

line = F.readline()
print(line)

line = F.readline()
print(line)

line1 = line.split("$")

print(line1)

print(eval(line1[0]))
print(eval(line1[1]))

line2 = [eval(P) for P in line1]
print(line2)
D = {'name':'tony','age':100}

F = open("demo47_3.txt","wb")

import pickle

pickle.dump(D,F)

F.close()
F = open("demo47_3.txt","rb")
import pickle

D = pickle.load(F)

print(D)
F = open("demo47_4.txt","wb")
import struct

data = struct.pack('>i4sh',8,'chinese',9)
print(data)

F.write(data)
F.close()

"""

with open("demo47_1.xml","r") as myfile:
    for line in myfile:
        print(line)




