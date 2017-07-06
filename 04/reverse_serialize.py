# 第一种方法
# f = open("file", "r")
# info = eval(f.read())
# print(info, type(info))
# print(info["age"])
# f.close()


# 第二种方法 推荐
# import json
#
# f = open("file", "r")
# info = json.loads(f.read())
# print(info, type(info))
# print(info["age"])
# f.close()


# 第三种方法
import pickle


def fun():
    print("bbb")


f = open("file", "rb")
# info = pickle.loads(f.read())
info = pickle.load(f)
print(info, type(info))
print(info["age"])
info["funname"]()
f.close()
