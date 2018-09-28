from multiprocessing import Process,Queue
import os

def run(name):
    print("子进程%s启动"%os.getpid())
    print("子进程在这里玩了一伙儿就走了")


if __name__=='__main__':

    print("主进程开始启动了%s"%os.getpid())
    p1 = Process(target=run,args=('tony',))
    p1.start()


    p2 = Process(target=run,args=('tom',))
    p2.start()
    p1.join()
    p2.join()
    print("主进程活干完了，休息了")

