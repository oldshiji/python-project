import threading
from multiprocessing import Process,Queue
import os,time

money = 0#金钱

'''
1、线程锁定　local线程　解决数据混乱
２、事件线程　　由事件驱动的线程
３、信号量线程　　控制线程并发执行数量
４、栅栏线程　　　控制线各累加多少后并发执行
５、线程调度　　　类似同步
６、线程通信　　　列队通信
7、定时线程
'''

bar = threading.Barrier(2)
def run(i):
    print("bank子线程%d启动"%(i))

    print("bank%d银行在处理数据"%(i))
    print("bank子线程%d结束"%(i))



def bank():
        for i in range(10):
            t = threading.Thread(target=run,args=(i,))
            t.start()
            t.join()


if __name__=='__main__':

    bank()




