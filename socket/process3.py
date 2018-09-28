from multiprocessing import Process,Pool,Queue
import time,os


def send(d):
    words = [1,2,3,4,5]
    for item in words:
        d.put(item)

def show(d):

    while True:
        words = d.get()
        if words:
            print("对方发来的费话是：%s"%(words))
        else:
            print("对方一个屁也没有放....")


if __name__=='__main__':

    print("父进程启动准备传输数据.....")
    '''
        p = Pool(2)
    p.apply_async(send)
    p.apply_async(show)
    p.close()
    p.join()
    '''
    d = Queue()


    sends = Process(target=send,args=(d,))
    shows= Process(target=show,args=(d,))

    sends.start()
    shows.start()
    sends.join()
    #shows.join()
    shows.terminate()

    print("父进程结束了")
