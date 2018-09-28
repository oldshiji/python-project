from multiprocessing import Process,Pool,Queue
import os,time
def show(a):
    print("子进程%s开始"%(os.getpid()))
    print("给么过xiao卖")
    time.sleep(1)
    print("子进程%s结束了"%(os.getpid()))

def talk(b):
    print("talk子进程开始%s"%(os.getpid()))
    print("孤呆的var")
    time.sleep(1)
    print("talk子进程结束%s"%(os.getpid()))



if __name__=='__main__':

    print("主进程开始")
    print("主进程id%s"%(os.getpid()))
    p1 = Process(target=show,args=(1,))
    p2 = Process(target=talk,args=(2,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("主进程结束")