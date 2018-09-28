from multiprocessing import Process,Queue
import os

def run(d):
    print("处理进程%s启动"%os.getpid())

    while True:
        data = d.get()
        if data:
            print("我消费了%d"%data)
        else:
            print("啥玩意也没有")


def callsb(d):
    print("产生进程启动了%s"%os.getpid())
    for i in range(1,10):
        print("开始产生数据%df"%i)
        d.put(i)
if __name__=='__main__':

    d = Queue()

    print("主进程开始启动了%s"%os.getpid())
    p1 = Process(target=callsb,args=(d,))
    p1.start()


    p2 = Process(target=run,args=(d,))
    p2.start()
    p1.join()
    #p2.join()

    p2.terminate()
    print("主进程活干完了，休息了")

