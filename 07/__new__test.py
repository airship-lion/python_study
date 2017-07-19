class MyType(type):
    def __init__(self):
        pass
        # super(MyType, self).__init__()

    def __call__(self, *args, **kwargs):
        obj = self.__new__(self, *args, **kwargs)
        self.__init__(obj, *args, **kwargs)


# 创建类的第一种方法
class Foo:
    __metaclass__ = MyType

    def talk(self):
        print("talk", self.name)

    def __init__(self, name):
        print('__init__')
        self.name = name

    def __new__(cls, *args, **kwargs):
        print('__new__')
        return object.__new__(cls)


# self.name = name
# 创建类的第二种方法
# def talk(self):
#     print("talk",self.name)
#
#
# def __init__(self, name):
#     self.name = name
#
#
# Foo = type('Foo', (), {'talk': talk, '__init__': __init__})

f = Foo('sdf')
f.talk()
