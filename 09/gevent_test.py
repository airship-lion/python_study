import gevent as gevent


def fun1():
    print('12')
    gevent.sleep(2)
    print('34')
    gevent.sleep(0.5)


def fun2():
    print('56')
    gevent.sleep(0.5)
    print('78')
    gevent.sleep(2)
    print('90')


def fun3():
    print('aa')
    gevent.sleep(0)
    print('bb')


gevent.joinall(
    [
        gevent.spawn(fun1)
        , gevent.spawn(fun2)
        , gevent.spawn(fun3)
    ]
)
