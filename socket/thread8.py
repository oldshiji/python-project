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
#线程调度
con = threading.Condition()


def bank():
    print("银行%s线程启动"%(threading.current_thread().name))
    for i in range(10):
        print("存款%d"%(i))

        con.notify()
        con.wait()

    print("银行%s线程结束"%(threading.current_thread().name))


def customer():
    print("客户%s线程启动"%(threading.current_thread().name))
    for i in range(10):
        print("取款%d"%i)
        time.sleep(1)
        con.notify()
        con.wait()

    print("客户%s线程启动"%(threading.current_thread().name))


if __name__=='__main__':

    print("主线程启动准备做事")
    t1 = threading.Thread(target=bank)
    t2 = threading.Thread(target=customer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("主线程结束")




