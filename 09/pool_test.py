import os
import time
from multiprocessing.pool import Pool

from multiprocessing import freeze_support



def run(n):
    print("run", n)
    time.sleep(0.2)
    print("finish", n)
    return n + 100


def cb(n):
    print('cb', n, os.getpid())
    # print('cb')


if __name__ == '__main__':
    # freeze_support()
    pool = Pool(5)
    for i in range(10):
        # pool.apply(func=run, args=(i,))
        pool.apply_async(func=run, args=(i,), callback=cb)

    print("finish", os.getpid())
    pool.close()
    pool.join()