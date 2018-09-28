import threading

def show():
    print('时间到了')




time = threading.Timer(5,show)
time.start()