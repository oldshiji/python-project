import time


def showtime()->'显示时间':
    return time.strftime('%Y-%m-%d',time.localtime(time.time()))


print(showtime())