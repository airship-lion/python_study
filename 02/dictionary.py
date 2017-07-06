dic = {"name1": "lily", "name2": "lucy"}
print(dic)
dic["name1"] = "tom"
dic["name3"] = "jim"
print(dic)
del dic["name1"]
print(dic)
dic.pop("name2")
print(dic)
dic["name5"] = "ben"
dic["name4"] = "alex"
dic.popitem()
print(dic)
print(dic["name5"])
print(dic.get("name5"))
print(dic.get("name6"))
# print(dic["name6"])
print("###".center(50, "-"))
for key in dic:
    print(key, dic[key])
print("###".center(50, "-"))
for index, key in enumerate(dic):
    print(index, key)
print("###".center(50, "-"))
for item in enumerate(dic):
    print(item)
print("###".center(50, "-"))
print(dic.keys())
print(dic.values())
print(dic.items())
print("###".center(50, "-"))
for key in dic.keys():
    print(key)
print("###".center(50, "-"))
for val in dic.values():
    print(val)
print("###".center(50, "-"))
for key, val in dic.items():
    print(key, val)
print("###".center(50, "-"))
d = dict.fromkeys([1, 2, 3], "sdfl")
d[1] = "aaa"
print(d)
print("###".center(50, "-"))
f = dict.fromkeys([1, 2, 3], [111, {"name": "jim"}])
f[1][0] = 222
f[1][1]["name"] = "tom"
print(f)

nation = {
    "广东": {
        "江门": {}, "广州": {}
    },
    "四川": {
        "成都": {}, "色达": {}
    },
    "贵州": {
        "贵阳": {}, "安顺": {}
    },
}
print(nation)
