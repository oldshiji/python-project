# -*- coding: utf-8 -*-

from multiprocessing import cpu_count
import threading
from time import sleep


class MyThread(threading.Thread):
    def __init__(self, name=None):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        super().run()
        for item in range(10000000):
            sleep(1)
            print("======={}=======> :{}".format(self.name, item))


if __name__ == "__main__":

    for i in range(500):
        MyThread(name=i).start()
