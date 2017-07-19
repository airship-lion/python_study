import threading
import time

num = 0
lock = threading.Lock()
# semaphore = threading.Semaphore(10)
semaphore = threading.BoundedSemaphore(3)


# def run(n):
#     print("run", n)
#     lock.acquire()
#     global num
#     num += 1
#     time.sleep(0.01)
#     lock.release()
#     print("finish", n)

def run(n):
    print("run", n)
    semaphore.acquire()
    global num
    num += 1
    time.sleep(0.5)
    semaphore.release()
    print("finish", n)


list1 = []
for i in range(500):
    t = threading.Thread(target=run, args={i})
    list1.append(t)
    t.start()

for t in list1:
    t.join()
# t1 = threading.Thread(target=run, args={1})
# t2 = threading.Thread(target=run, args={2, })
# t1.setDaemon(True)
# t1.start()
# # t1.join()
# t2.start()
# t1.join()
# t2.join()

# run(1)
# run(2)
print("main finish", num)
