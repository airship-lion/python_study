def fun(x):
    return x ** 2 + 1


# x = [i * 2 for i in range(10)]
x = [fun(i) for i in range(10)]
y = (fun(i) for i in range(10))
print(x)
print(y)
print(x[3])
# print(y[0])
print(y.__next__())
print(y.__next__())
print(y.__next__())
for i in y:
    print(i)


# 生成器
def fib(n):
    i, a, b = 0, 0, 1
    while i < n:
        c = yield (b)
        print(c)
        a, b = b, a + b
        i += 1


print("----------")
fib1 = fib(10)
print(fib1)
print(fib1.__next__())
print("aaaa")
print(fib1.send("send"))  # c接收send的值，并也会相对于调用了__next__方法
print("bbbb")
print(fib1.__next__())
print("cccc")
print(fib1.__next__())
print("dddd")
print(fib1.__next__())
