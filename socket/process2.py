from multiprocessing import Pool,Queue
import time,os


def playMobile(mobile):
    print("玩手机进程启动%s"%(os.getpid()))

    time.sleep(1)
    for i in range(0,5):
        print("我在玩手机中,手机是%s" % (mobile))
        time.sleep(1)
        print(time.strftime('%Y-%m-%d %H:%I:S', time.localtime(time.time())))


    print("玩手机进程结束%s"%(os.getpid()))

def playGame(game):
    print("打游戏进程启动%s"%(os.getpid()))
    time.sleep(1)
    for i in range(0,6):
        print("我正在打%s游戏" % (game))
        time.sleep(1)
        print(time.strftime('%Y-%m-%d %H:%I:S', time.localtime(time.time())))

    print("打游戏进程结束%s"%(os.getpid()))



if __name__=='__main__':

    print("主进程启动准备搞事")
    p = Pool(2)
    p.apply_async(playMobile,args=('IphoneX',))
    p.apply_async(playGame,args=('吃j',))

    p.close()
    p.join()
    print("主进程结束了")


