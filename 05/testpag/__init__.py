# 如果入口是本目录下可以这样导入，但是是其他目录下的不可以
# import test1


# 如果入口是其他目录下可以这样导入，但是是本目录下的不可以
from . import test2
from . import test_main

print("from init")
