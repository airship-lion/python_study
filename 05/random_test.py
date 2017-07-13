import random

print(random.random())
print(random.uniform(1, 3))
print(random.randint(1, 3))
print(random.randrange(1, 3))
print(random.choice([1, 2, 3]))
print(random.choice("abcde"))
print(random.sample("abcde123", 4))
list1=[1, 2, 3, 4, 5, 6, 7]
random.shuffle(list1)
print(list1)
