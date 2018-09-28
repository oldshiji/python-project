

def f1(n):
    a,b=0,1
    while a < n:
        print(a,end='')
        a,b=b,a+b
    print()



def f2(n):
    result = []
    a,b=0,1
    while a<n:
        result.append(a)
        a,b=b,a+b

    return result



if __name__ == "__main__":
    import sys
    #print(sys.argv[1])
    num = int(sys.argv[1])

    #print(type(int(num)))
    #print(num)
    f1(num)




