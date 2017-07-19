import traceback


class MyExeption(Exception):
    def __init__(self, name):
        self.message = name

    # def __str__(self):
    #     return 'sdfsdf'
    #     # return self.message


data = [1, 2, 3]
map1 = {}

try:
    a = {"age": 22}
    raise MyExeption("自定义错误")
    data[4]
    map1["age"]

# except IndexError as e:
#     print("IndexError ", e)
except KeyError as e:
    print("KeyError", e)
except Exception as e:
    # print("出错了", e)
    # print('str(Exception):\t', str(Exception))
    # print('str(e):\t\t', str(e))
    # print('repr(e):\t', repr(e))
    # print(traceback._cause_message)
    # print(traceback._context_message)
    # traceback.format_exc()
    traceback.print_exc()  # 这两个打印信息一样traceback.print_exc(),traceback.format_exc(),不过前者不需print，而且前者在pycharm中打印信息是红色的
    # print(traceback.format_exc())
else:
    print(a)
finally:
    print("finally")
