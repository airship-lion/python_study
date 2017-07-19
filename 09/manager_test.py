import os

from multiprocessing import Manager, Process


def run(dic, li):
    dic[os.getpid()] = os.getpid()
    li.append(os.getpid())
    print(li)


if __name__ == '__main__':
    with Manager() as manager:
        dic = manager.dict()
        li = manager.list()
        liP = []
        for i in range(10):
            p = Process(target=run, args=(dic, li))
            liP.append(p)
            p.start()
        for p in liP:
            p.join()
        print(dic)
        print(li)
