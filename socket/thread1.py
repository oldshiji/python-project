import threading
from multiprocessing import Process,Queue
import os,time

'''
1、线程锁定　local线程　解决数据混乱
２、事件线程　　由事件驱动的线程
３、信号量线程　　控制线程并发执行数量
４、栅栏线程　　　控制线各累加多少后并发执行
５、线程调度　　　类似同步
６、线程通信　　　列队通信
7、定时线程
'''
def play(a):
    print("play子线程%s启动"%(threading.current_thread().name))
    time.sleep(1)
    print("play子线程%s结束"%(threading.current_thread().name))

def doing(b):
    print("doing子线程%s启动"%(threading.current_thread().name))
    time.sleep(1)
    print("tash is over")
    print("doing子线程结束%s"%(threading.current_thread().name))

if __name__=='__main__':

    print("主线程启动")
    t1 = threading.Thread(target=play,args=(1,))
    t2 = threading.Thread(target=doing,args=(2,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("主线程结束")


