import sys
import random


x = random.random()

if x < 10:
    print('x lt 10',x)
elif x ==10:
    print('x eq 10',x)
elif x >10:
    print('x gt 10',x)
else:
    print('x is default',x)


def compare(x,y,type):
    if type == 'eq':
        if x == y:
            return 'eq'
        else:
            return 'not eq'
    elif type == 'gt':
        if x>y:
            return 'gt'
        else:
            return 'not gt'
    elif type == 'lt':
        if x < y:
            return 'lt'
        else:
            return 'not lt'
    else:
        return 'not compare'



print(compare(1,3,'eq'))

中文='chinese'
print(中文)