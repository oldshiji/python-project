

l1 = [1,2,3,4]
l2 = [5,6,7,8]

"""

print(zip(l1,l2))

print(list(zip(l1,l2)))
for x,y in list(zip(l1,l2)):
    print(x,y,x+y,end='\n')
    t1,t2,t3 = (1,2,3),(4,5,6),(7,8,9)

for x,y,z in list(zip(t1,t2,t3)):
    print(x,y,z,x+y+z,end='\n')
    s1,s2 = 'abc','zyx123'

for x,y in list(zip(s1,s2)):
    print(x,y,x.upper(),y.upper(),end='\n')
keys = ['chinese','japanese','america']
vals = ['5000','1000','200']
D = {}
for (k,v) in list(zip(keys,vals)):
    D[k] = v

print(D)

keys  = ['chinese','america','indea']
vals = ['13','1','12']

print(dict(zip(keys,vals)))
s = 'spam'
offset = 0
for item in s:
    print(item,'this letter of offset:',offset)
    offset+=1
    s = 'spam'
for x in range(0,len(s),1):
    print(s[x],'the leffter of offset:',x)
    
for (item,offset) in enumerate(s):
    print(item,'appears of offset:',offset)

"""

s = 'spam'
e = enumerate(s)
print(next(e))
print(next(e))
print(next(e))
