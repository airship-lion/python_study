import time


def timer(fun):
    def deco(*args, **kwargs):
        start_time = time.time()
        print("timer before")
        res = fun(*args, **kwargs)
        print("timer after")
        end_time = time.time()
        # print("timer cost  time %s" % (end_time - start_time))
        return res

    return deco


def funtype1():
    print("if funtype 1")


def funtype2():
    print("if funtype 2")


def timer2(funtype):
    # print("funtype : ", funtype)

    def outdeco(fun):
        def deco(*args, **kwargs):
            if funtype == 1:
                funtype1()
            else:
                funtype2()
            start_time = time.time()
            print("timer2 before")
            res = fun(*args, **kwargs)
            print("timer2 after")
            end_time = time.time()
            # print("cost time %s" % (end_time - start_time))
            return res

        return deco

    return outdeco


@timer
@timer2(funtype=1)
def test1():
    print("test1")
    return "test1 res"


@timer2(funtype=2)
@timer
def test2(name):
    print("test2 " + name)
    return "test2 res"


def deco(fun):
    start_time = time.time()
    fun()
    end_time = time.time()
    print("cost time %s" % (end_time - start_time))


# test1 = timer(test1)
# test2 = timer(test2)
print(test1())
print("-----------")
print(test2("lily"))
# timer(test1)()
# timer(test2)()

# deco(test1)
