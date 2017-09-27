# 1 1 2 3 5 8
def fib(num):
    if (num < 1):
        return
    
    seed = [1, 1]
    
    while seed[len(seed) - 1] <= num:
        length = len(seed)
        seed.append(seed[length - 1] + seed[length - 2])
    
    seed.pop()
    print(seed)

def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

def angle():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i] + L[i - 1] for i in range(len(L))]

# name = ['adame', 'baby', 'lisa']

from functools import reduce

def normalize(name):
    def formater(s):
        return s[0:1].upper() + s[1:].lower()
    return map(formater, name)

def prod(l):
    def fn(x, y):
        return x * y
    return reduce(fn, l)
def str2float(s):

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    def numlist2num(x, y):
        return x * 10 + y

    def padZero(num):
        ten = 1
        x = 0
        l = len(str(num))
        while x < l:
            ten = ten * 10
            x = x + 1
        return ten
        
    list0 = s.split('.')
    list1, list2 = list0[0], list0[1]

    num1 = reduce(numlist2num, map(char2num, list1))
    num2 = reduce(numlist2num, map(char2num, list2))

    return num1 + (num2 / padZero(num2))

def isOdd(num):
    return num % 2 == 0
# filter(isOdd, [1, 2, 3.4, 5, 6])

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：

def _join(x, y):
    return x + y

def is_palindrome(n):
    s = str(n)
    l = len(s)
    n = 0
    while n < int(l / 2):
        if s[n] != s[l - n - 1]:
            return False
        n = n + 1
    return True

# 有一种更加简便的方法 [::-1]这个方法可以直接将字符串颠倒
# def is_palindrome(n):
#     return str(n) == str(n)[::-1]

# ====
# 假设我们用一组tuple表示学生名字和成绩：L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]; 请用sorted()对上述列表分别按名字排序：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]
def by_score(t):
    return t[1]

# python 中的闭包 'Closure' 内部函数可以引用外部函数的参数和局部变量
# 
# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# 
# 这个与 js 很像
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)

    return fs


# 如果一定要引用循环变量
def new_count():
    fs = []
    f = lambda x: lambda: x * x
    for i in range(1, 4):
        fs.append(f(i))
    return fs

# 看到一个同学写的不错，有点老衲的风范
def _new_count():
    return map(lambda x: lambda: x * x, range(1, 4))

# 匿名函数这一节，评论中有一个小弟提的问题，最后修改的答案
def multipliers(i):
    return map(lambda x: lambda: i * x, range(1, 4))


# 装饰函数
import functools

def log(text):
    def decorator(fn):
        # 这里 @ 操作，相当于 wrapper.__name__ = fn.__name__
        @functools.wraps(fn)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, fn.__name__))
            return fn(*args, **kw)
        return wrapper
    return decorator