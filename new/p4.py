from multiprocessing import Process,Pool,Queue
import os
import time
def run(i):
    print("子进程%d启动--%s"%(i,os.getpid()))
    print("我在这里睡一伙儿")
    time.sleep(3)
    print("子进程%d--%s结束"%(i,os.getpid()))


if __name__=='__main__':
    print("主进程启动%s"%(os.getpid()))
    pool = Pool(3)

    for i in range(0,3):
        pool.apply_async(run,args=(i,))

    pool.close()

    pool.join()

    print("主进程结束了")


