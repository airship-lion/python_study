import multiprocessing
import threading

import time

from multiprocessing import Queue


# from queue import Queue
# from multiprocessing.queues import Queue


def run(n):
    print("run", n)
    time.sleep(1)
    print("finish", n)


def conn(q):
    q.put(1)
    print('conn')


li = []

if __name__ == '__main__':  # 在windows里多进程必须写这句，不然报错
    for i in range(1):
        q = Queue()
        # p = threading.Thread(target=conn, args=())
        # 多进程队列才可以用于进程中通信
        p = multiprocessing.Process(target=conn, args=(q,))
        li.append(p)
        p.start()
        print(q.get())

for p in li:
    p.join()
