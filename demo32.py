import time
import math

""""
a = 123

print(a)
print(type(a))
print(str(a))
print(type(str(a)))

#print("hello"+a)
print("hello"+str(a))
print("jack"+repr(a))

for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(6),end='')
    print(repr(x*x*x).rjust(4))
    
for x in range(1,11):
    #print('{0:1d} {1:2d} {2:3d}'.format(x,x*x,x*x*x))
    print('{0:1d} {1:2d} {2:3d}' % (x,x*x,x*x*x))
    
print('3'.zfill(5))

print('-0.003'.zfill(5))

print("there are some {},will cost {}".format("eggs","100dollars"))

print("{0} and {1}".format("famle","male"))

print("{1} and {0}".format("female","male"))


print("these eggs will cost {money} and its weight is {weight}".format(money="100块",weight="100KG"))
print("in these cases will have some {0} and {1},so try {a}".format("erros","warning",a="处理"))
print("there are {} eggs in the blanket".format(math.pi))
print("there are {!a}".format(math.pi))
print("there is {!s}".format(math.pi))
print("there are {!r}".format(math.pi))
pi = math.pi

print(pi)
print(type(pi))

print(str(pi))
print(type(str(pi)))

print(repr(pi))
print(type(repr(pi)))

print()
"""

print("the float number is {0:.3f}".format(math.pi))
