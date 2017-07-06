count = 0
while count < 100:
    count += 1
    print(count)
    # if count == 100:
    if count == 101:
        break
else:
    print("aaa")
print("bbb")

for i in range(2, 10):
    print("for : ", i)
print("-------")
for i in range(10, 2, -1):
    print("for : 可是对方", i)
