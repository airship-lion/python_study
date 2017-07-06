def fun1(x, y, z):
    print(x)
    print(y)
    print(z)


def fun2(x, y, z=2):
    print(x)
    print(y)
    print(z)


def fun3(*args):
    print(args)


fun1(1, 2, 3)
fun1(1, y=33, z=44)
# fun1(1, 44, y=33)
print("----------")
fun2(111, 222)
fun2(111, 222, 333)
fun2(111, y=222)
print("----------")
fun3(1, 2, 3)
fun3([1, 2, 3])
fun3([1, 2, 3], 44)
fun3(*[1, 2, 3])
fun3(*[1, 2, 3, (44, 55)])
fun3(*[1, 2, 3, [44, 55]])
fun3()
fun3(*())

print("----------")


def fun4(**kwargs):
    print(kwargs)
    print(kwargs["name"])


fun4(name="lily", age=22, gender=False)
fun4(**{"name": "lily", "age": 22, "gender": False})

print("----------")


def fun5(x, y, *args):
    print(x)
    print(y)
    print(args)


fun5(1, 2, 3, 4, 5)
# fun5(x=1,y= 2, 3, 4, 5)
# fun5(3, 4, 5, x=1, y=2)

print("-----6-----")


def fun6(*args, x, y):
    print(x)
    print(y)
    print(args)


fun6(1, 2, 3, x=4, y=5)
fun6(x=4, y=5)
# fun6(1, 2, 3)

print("-----7-----")


def fun7(x, y, **kwargs):
    print(x)
    print(y)
    print(kwargs)
    # print(kwargs["name"])


fun7(33, 44, name="lily", age=22, gender=False)
# fun7(x=33, y=44, name="lily", age=22, gender=False)
# fun7(x=33, y=44, **{"name": "lily", "age": 22, "gender": False})
# fun7(**{"x": 33, "y": 44, "name": "lily", "age": 22, "gender": False})
# fun7(33, 44, **{"x": 33, "y": 44, "name": "lily", "age": 22, "gender": False})
print("-----8-----")


def fun8(x, y=2, *args):
    print(x)
    print(y)
    print(args)


fun8(1, 3, 4, 5)
# fun8(1, 3, 4, y=5)
# fun8(1, y=3, 4, 5)

print("-----9-----")


def fun9(x, *args, y):
    print(x)
    print(y)
    print(args)


# fun9(1, 33, 44, 666)
fun9(1, 33, 44, y=666)
print("-----10-----")


def fun10(x, *args, y=2):
    print(x)
    print(y)
    print(args)


fun10(22, 33, 444, y=555)

print("-----11-----")


def fun11(x, y=2, **kwargs):
    print(x)
    print(y)
    print(kwargs)


fun11(2, 3, name="lily")
fun11(2, name="lily")
fun11(2, y=3, name="lily")
fun11(2, y=3, **{"name": "lily"})

print("-----12-----")

# def fun12(x, **kwargs, y):
#     print(x)
#     print(y)
#     print(kwargs)
print("-----13-----")


def fun13(x, y=2, *args, **kwargs):
    print(x)
    print(y)
    print(args)
    print(kwargs)


fun13(1, 3, 44, 33, name="tom", age=12)
# fun13(1, *[44, 33], name="tom", age=12, y=3)
fun13(1, name="tom", age=12, y=3)
fun13(1, *[44, 33], name="tom", age=12)
fun13(1, *(44, 33), name="tom", age=12)


def a():
    print("a")
    b()


def b():
    print("b")


a()
