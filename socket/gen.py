

def run():
    data = ""
    #
    # try:
    #     r = yield data
    #     print(r, data)
    #     r1 = yield data
    #     print(r, data)
    #     r2 = yield data
    #     print(r, data)
    # except StopIteration as e:
    #     pass

    for i in range(0,10):
        r = yield i
        print(r,i)

if __name__=='__main__':

    gen = run()
    # gen.send(None)
    # gen.send('hi')
    # gen.send('hello')

    # for j in list(range(0,10)):
    #     print(gen is iter(gen))
    #     next(gen)
    gen.send(None)
    gen.send(100)
    gen.send(200)
