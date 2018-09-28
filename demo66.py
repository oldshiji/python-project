import multiprocessing
import os

def run_proce(name):
    print('child process {0}{1} running'.format(name,os.getpid()))




if __name__ == '__main__':

    print("parent process {0} start".format(os.getpid()))
    for i in range(5):
        p = multiprocessing.Process(target=run_proce,args=(i,))
        print('process start')
        p.start()

    p.join()
    print('process close')

