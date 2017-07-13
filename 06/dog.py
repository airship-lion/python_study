class Dog:
    n = 123
    name = "tom"

    def __init__(self, name):
        self.name = name
        self.gender = False
        self.__dog_type = "金毛"  # 私有属性

    def get_dog_type(self):
        return self.__dog_type

    def __private_fun1(self):
        print("__private_fun1")

    def public_fun1(self):
        print("public_fun1")
        __private_fun1(self)

    def __del__(self):
        print("析构方法", self.name)

    def speak(self):
        print(self.name, "wang")


print(Dog.n)
print(Dog.name)
Dog.n += 1
print(Dog.n)
dog = Dog("旺财")
dog.speak()
dog.n += 1
print(dog.name, dog.n)
del dog
# Dog.speak(dog)
dog2 = Dog("小白")
dog2.age = 3
print(dog2.age)
# print(dog.age)
# print(dog.gender)
# del dog.gender
# print(dog.gender)
print(dog2.gender)
print(dog2.get_dog_type())
dog2.public_fun1()
