# import moduleFun
#
# moduleFun.module_fun1()

# from moduleFun import module_fun1
#
# module_fun1()


# 导本目录的文件这种不行
# from . import moduleFun
#
# moduleFun.module_fun1()

import testpag

# test1_fun1()
# test1.test1_fun1()
testpag.test1.test1_fun1()
# myfun1()
# test_main.myfun1()
testpag.test_main.myfun1()

import importlib

test1 = importlib.import_module("testpag.test1")
test1.test1_fun1()
