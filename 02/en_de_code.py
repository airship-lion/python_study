msg = "你好"
print(msg,type(msg))
# print(msg.decode())
print(msg.encode(),type(msg.encode()))
print(msg.encode("utf-8"))
print(msg.encode(encoding="utf-8").decode("gbk"))
print(msg.encode(encoding="gbk").decode("gbk"))
print(msg.encode(encoding="utf-8").decode("utf-8"))
