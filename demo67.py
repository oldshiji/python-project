

"""
def mysum(l):
    if not l:
        return 0
    else:
        return l[0]+mysum(l[1:])
        '''
        第一次运行时
        l[0]=1
        l[1:]=[2,3,4,5,6]
        l[0]=2
        l[1:]=[3,4,5]
        l[0]=3
        l[1:]=[4,5]
        l[0]=4
        l[1:]=5
        l[0]=5
        '''


print(mysum([1,2,3,4,5]))
l = [1,2,3,4,5]
sum = 0
while l:
    sum+=l[0]
    l=l[1:]

print(sum)
sum = 0
for x in list(range(5)):
    sum+=x

print(sum)
"""

def mysumtree(L):
    print(L)
    total = 0
    for x in L:
        if not isinstance(x,list):
            total+=x
        else:
            total+=mysumtree(x)

    return total


print(mysumtree([1,[2,[3,4],5],6,[7,8]]))