import copy

names = ["aaa", "bbb", "ccc", "ddd"]

names.append("eee")
names.insert(2, "fff")
print(names[1])
print(names[1:3])
print(names[-1])
print(names[-2])
print(names[-3:-1])
print(names[-1:-3])
print(names[-3:])
print(names[1:])
print(names[0:3])
print(names[:3])
print("names[:]", names[:])
print("names[0:4:2]", names[0:4:2])
print("names[::2]", names[::2])
print("names[:4:]", names[:4:])
print(names)
names[2] = "ggg"
print(names)
names.remove("ggg")
print(names)
del names[1]
print(names)
names.pop(2)
print(names)
# del names
# names.clear()
# print(names)
# print(names.index("fff"))
# names.index("fff")
print(names.count("eee"))
print(names.count("ff"))
names.reverse()
print(names)
names.sort()
print(names)
names.sort(reverse=True)
print(names)
names.sort(reverse=False)
print(names)
names2 = [1, 2, 3, 4]
names.extend(names2)
print(names)
names_copy = names.copy()
print(names_copy)
names.append(["lily", "tom"])
print(names)
names_copy = names.copy()
names_copy2 = names[:]
names_copy3 = list(names)
name_deepcopy = copy.deepcopy(names)
print(names_copy)
print(names_copy2)
print(names_copy3)
print(name_deepcopy)
names[1] = "fff"
names[-1][0] = "lucy"
print(names)
print(names_copy)
print(name_deepcopy)
print("------------0----------------")
for item in names:
    print(item)
print("------------1----------------")
for index, item in enumerate(names):
    print(index, item)
print("-------------2---------------")
for item in enumerate(names):
    print(item,type(item))
print("-------------3---------------")
kk = [[111, "222", "jjj"], [222, "333", "kkk"]]
for key, val, val2 in kk:
    print(key, val)
print("-------------4---------------")
for item in kk:
    print(item)
