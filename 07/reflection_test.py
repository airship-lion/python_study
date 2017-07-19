def haha(self):
    print(" %s is haha" % self.name)


class Dog:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(" %s is talk" % self.name)


d = Dog("tom")
# d.talk()
choi = input("input : ")
if hasattr(d, choi):
    getattr(d, choi)()

else:
    setattr(d, choi, haha)
    getattr(d, choi)(d)
