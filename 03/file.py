file = open("file1", encoding="utf-8", mode="r")
# print(file.readlines())
for line2 in file:
    print(line2)
for idx, line in enumerate(file.readlines()):
    if idx == 2:
        continue
    print(line)
for i in range(5):
    print(file.readline())
data = file.read()
data2 = file.read()
print(data)
print("--------------------")
print(data2)

file2 = open("file2", encoding="utf-8", mode="a")
file2.write("都是浪费时间的罚款收据......\n")
file2.write("都加上地方妓女是........\n")
