from multiprocessing import Process,Queue
import os

num = 100
def run(num):
    print("处理进程%s启动"%os.getpid())

    num+=200
    print("处理进程的结果是%d"%num)

def callsb(num):
    print("产生进程启动了%s"%os.getpid())
    num+=300
    print("产生进程的结果是%d"%num)


if __name__=='__main__':

    d = Queue()

    print("主进程开始启动了%s"%os.getpid())
    p1 = Process(target=callsb,args=(num,))
    p1.start()


    p2 = Process(target=run,args=(num,))
    p2.start()
    p1.join()
    p2.join()


    print("主进程活干完了，休息了")

