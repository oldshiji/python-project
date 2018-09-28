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
#线程local
event = threading.Event()
#print(dir(lock))
def bank(a,local):
    print("play子线程%s启动"%(threading.current_thread().name))


    for i in range(1, 10000000):
        # lock.acquire()
        event.wait() #等待事件触发此线程运行
        local += 1
        local -= 1
        event.clear()#执行之后，事件重
        print("bank线程运行中[线程事件运行].....")
        # lock.release()



    print("存款%d万"%local)


    print("play子线程%s结束"%(threading.current_thread().name))

def customer(b,local):
    print("doing子线程%s启动"%(threading.current_thread().name))

    for i in range(1, 10000000):
        # lock.acquire()
        event.set()
        local += 1
        local -= 1
        time.sleep(2) #２秒钟触发其它线程执行
        print("customer线程运行中[线程事件源触发]....")
        # lock.release()

    print("我取了%d万元人民币"%local)

    print("doing子线程结束%s"%(threading.current_thread().name))

if __name__=='__main__':

    print("主线程启动")

    t1 = threading.Thread(target=bank,args=(1,money))
    t2 = threading.Thread(target=customer,args=(2,money))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("银行还有%d万存款"%(money))
    print("主线程结束")



