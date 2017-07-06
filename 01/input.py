import getpass

name = input("name:")
pwd = input("pwd:")
age = int(input("age:"))
psw = getpass.getpass("psw:")
"""
print(name)
"""
# print(name)
# print(pwd)
# info = "name : " + name + "   pwd : " + pwd
info1 = '''name : %s    pwd : %s     age : %d''' % (name, pwd, age)
info2 = '''name : {_name}    pwd : {_pwd}     age : {_age}'''.format(_name=name, _pwd=pwd, _age=age)
info3 = '''name : {0}    pwd : {1}     age : {2}'''.format(name, pwd, age)
# info = '''name : %s    pwd : %s'''
# info = \
#     'name : %s    pwd : %s \
#     '
# info = 'name : %s    pwd : %s  '
print(info1)
print(info2)
print(info3)
# print(info1, info3)
print(psw)
