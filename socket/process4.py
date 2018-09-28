from multiprocessing import Process,Pool,Queue
import time,os


def send(d):

    for i in range(0,5):
        d.put(i)



def show(d):

    for i in range(0,5):
        data = d.get()
        print(data)

if __name__=='__main__':

    d = Queue()
    print("父进程启动准备传输数据.....")
    '''
        p = Pool(2)
    p.apply_async(send)
    p.apply_async(show)
    p.close()
    p.join()
    '''

    sends = Process(target=send,args=(d,))
    shows= Process(target=show,args=(d,))
    sends.start()
    shows.start()
    sends.join()
    shows.join()

    print("父进程结束了")
