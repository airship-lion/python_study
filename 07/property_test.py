class Dog:
    def __init__(self):
        self.__name = None
        self.__age = None

    def get_name(self):
        print(self.__name)
        return self.__name

    def set_name(self, name):
        self.__name = name

    @property
    def age(self):
        print("property")
        print(self.__age)
        return self.__age

    @age.setter
    def age(self, age):
        print("setter")
        self.__age = age

    @age.getter  # 获取age时有getter进入getter，没有则进入property
    def age(self):
        print("getter")
        print(self.__age)
        return self.__age

    @age.deleter
    def age(self):
        print("deleter")
        del (self.__age)

    def __call__(self, *args, **kwargs):
        print("__call__", args, kwargs)

    def __str__(self):
        return self.__name


dog = Dog()
# dog.get_name()
dog.set_name("tom")
# dog.get_name()
a1 = dog.age
dog.age = 22
a2 = dog.age
# Dog.age
del dog.age
# dog.age
# Dog.age
dog(1, 2, 3, name="hhhh")
print(Dog.__dict__)
print(dog.__dict__)
print(dog)
