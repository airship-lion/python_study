import shutil

# shutil.copyfile("test111","test222")
# shutil.copystat("test111","test222")
# shutil.copytree("test_makedirs","test_makedirs2")
# shutil.rmtree("test_makedirs2")
shutil.make_archive("shutil_archive_test", "zip", r"C:\soft\PyCharmProjects\day01\05\test_makedirs\01")
