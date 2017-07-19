from multiprocessing import Process, Pipe

import time


def run(conn):
    print('run start')
    time.sleep(0.5)
    conn.send({'age': 22, 'name': 'tom'})
    conn.send({'age': 32, 'name': 'jim'})
    print(conn.recv())
    print('run end')


if __name__ == '__main__':
    conn1, conn2 = Pipe()
    p = Process(target=run, args=(conn2,))
    p.start()
    print(conn1.recv())
    print(conn1.recv())
    conn1.send('hello')
    p.join()
