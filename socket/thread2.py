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
#线程锁对象
lock = threading.Lock()
#print(dir(lock))
def bank(a):
    print("play子线程%s启动"%(threading.current_thread().name))
    global money
    with lock:
        for i in range(1, 10000000):
            # lock.acquire()
            money += 1
            money -= 1
            print("bank线程运行中.....")
            # lock.release()



    print("存款%d万"%money)


    print("play子线程%s结束"%(threading.current_thread().name))

def customer(b):
    print("doing子线程%s启动"%(threading.current_thread().name))

    global money
    with lock:
        for i in range(1, 10000000):
            # lock.acquire()
            money += 1
            money -= 1
            print("customer线程运行中....")
            # lock.release()

    print("我取了%d万元人民币"%money)

    print("doing子线程结束%s"%(threading.current_thread().name))

if __name__=='__main__':

    print("主线程启动")
    t1 = threading.Thread(target=bank,args=(1,))
    t2 = threading.Thread(target=customer,args=(2,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("银行还有%d万存款"%(money))
    print("主线程结束")


