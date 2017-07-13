class Dog:
    n = 3

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(self.name)

    @staticmethod
    def walk():
        # print("walk", n)
        print("walk")

    @classmethod
    def run(cls):
        print("walk", cls.n)


dog = Dog("tom")
dog.talk()
Dog.walk()
Dog.run()
