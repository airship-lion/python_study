from greenlet import greenlet


# 协程，应用管理的单元，CPU不知道它的存在，比线程的单元还要小
def fun1():
    print('12')
    gr2.switch()
    print('34')
    gr2.switch()


def fun2():
    print('56')
    gr1.switch()
    print('78')
    gr1.switch()


gr1 = greenlet(fun1)
gr2 = greenlet(fun2)
gr1.switch()
