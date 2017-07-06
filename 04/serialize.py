# 第一种方法
# f = open("file", "w")
# info = {"age": 22, "name": "tom"}
# print(info)
# print(str(info))
# f.write(str(info))
# f.close()


# 第二种方法 推荐
# import json
#
# f = open("file", "w")
# info = {"age": 23, "name": "lily"}
# print(info)
# f.write(json.dumps(info))
# f.close()


# 第三种方法
import pickle


def fun():
    print("aaa")


f = open("file", "wb")
info = {"age": 25, "name": "jim", "funname": fun}
print(info)
# f.write(pickle.dumps(info))
pickle.dump(info, f)
f.close()
