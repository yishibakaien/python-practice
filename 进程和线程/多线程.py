
import time, threading

# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
# 新线程执行代码：
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while (n < 5):
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
# => thread MainThread is running... 可以看出默认主线程 名叫 MainThread ?

t = threading.Thread(target = loop, name = 'LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
# thread MainThread is running...
# thread LoopThread is running...
# thread LoopThread >>> 1
# thread LoopThread >>> 2
# thread LoopThread >>> 3
# thread LoopThread >>> 4
# thread LoopThread >>> 5
# thread LoopThread ended.
# thread MainThread ended.


# Lock

import time, threading
# 假定这是你的银行存款
balance = 0
def change_it(n):
    # 先存后取， 结果应该为 0
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)

t1 = threading.Thread(target = run_thread, args = (5,))
t2 = threading.Thread(target = run_thread, args = (8,))

t1.start()
t2.start()
t1.join()
t2.join()

print(balance)

# 可见打印的结果不一定是 0
# 是因为修改balance需要多条语句， t1 和 t2 是交替运行的
# 而执行这几条语句时，线程可能中断，从而导致多个线程把同一个对象的内容改乱了。


# 去报 balance 计算正确，需要给线程上 '锁'

balance = 0
lock = threading.Lock()

def run_thread(n):
    for i in range(100000):
        # 先要获取锁
        lock.acquire()
        try:
            # 放心的改吧
            change_it(n)
        finally:
            lock.release()
