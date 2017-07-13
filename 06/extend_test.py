class Person(object):
    def __init__(self, name):
        print("init Person")
        self.name = name

    def eat(self):
        print("%s is eating " % self.name)

    def sleep(self):
        print("%s is sleep " % self.name)


class Animal(object):
    # def __init__(self):
    #     print("init Animal")
    #     # self.animal_name = animal_name

    def walk(self):
        print("walk")


class Man(Animal, Person):
    # def __init__(self, name, age):
    #     # Person.__init__(self, name)
    #     # Animal.__init__(self, name)
    #     # super(Man, self).__init__(name)
    #     super(Man, self).__init__()
    #     self.age = age
    #     print("init Man")

    def talk(self):
        print("%s is talk " % self.name)

    def sleep(self):
        Person.sleep(self)
        print("%s is sleep man" % self.name)


# man1 = Man("tom",22)
man1 = Man("tom")
# man1 = Man()
# man1.eat()
# man1.sleep()
# man1.talk()
man1.walk()


# print(man1.animal_name)
# print(man1.age)

class A:
    def __init__(self):
        print("a")


class B(A):
    pass
    # def __init__(self):
    #     print("b")


class C(A):
    pass
    # def __init__(self):
    #     print("c")


class D(B, C):
    pass
    # def __init__(self):
    #     print("d")

# 在python2里经典类是深度优先继承，新式类是广度优先继承
# 在python3里经典类和新式类都是广度优先继承
# 深度优先继承：继承顺序是:D->B->A
# 广度优先继承：继承顺序是:D->B->C->A
# 经典类：class A:
# 新式类: class A(object):
d = D()
