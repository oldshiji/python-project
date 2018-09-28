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

event = threading.Event()
local = threading.local()



def bank(a,local,d):
    print("play子线程%s启动"%(threading.current_thread().name))


    while True:
        print("等待客户存钱中....")
        event.wait()
        data = d.get()
        local+=data
        print("本次存款是%d"%(local))
        event.clear()

    print("存款%d万"%local)


    print("play子线程%s结束"%(threading.current_thread().name))

def customer(b,local,d):
    print("doing子线程%s启动"%(threading.current_thread().name))


    while True:
        money = int(input("请输入存款："))
        if money:
            d.put(money)
            event.set()

    print("doing子线程结束%s"%(threading.current_thread().name))

if __name__=='__main__':

    print("主线程启动")
    local.x = money

    d = Queue()

    t1 = threading.Thread(target=bank,args=(1,local.x,d))
    t2 = threading.Thread(target=customer,args=(2,local.x,d))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("银行还有%d万存款"%(local.x))
    print("主线程结束")



