import os
import sys

print(sys.path)
print(sys.argv[0])
print(sys.version_info)
# os.system("dir")
read = os.popen("dir").read()
print(read)
os.mkdir("new_dir")
