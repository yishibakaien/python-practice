import functools

# def log(fn):
#     @functools.wraps(fn)
#     def wrapper(*args, **kw):
#         print('begin call %s():' % fn.__name__)
#         a = fn(*args, **kw)
#         print('end call %s():' % fn.__name__)
#         return a
#     return wrapper

# @log
# def name(text):
#     print(text)
# name('陈某人天才1')
# print(name.__name__)

# 再思考一下能否写出一个@log的decorator，使它既支持传参，也支持不传参

def superLog(text):
    def decorator(fn):
        name = fn.__name__
        @functools.wraps(fn)  #这里可以改变 wrapper 的 __name__ 为 fn 的 __name__
        def wrapper(*args, **kw):
            if isinstance(text, str):
                print('%s begin %s():' % (text, name))
            else:
                print('begin %s():' % name)
            ret = fn(*args, **kw)
            if isinstance(text, str):
                print('%s end %s' % (text, name))
            else:
                print('end %s():' % (name))
            return ret
        # wrapper.__name__ = fn.__name__  在这里 也 可以改变 wrapper 的 __name__ 属性
        return wrapper
    return decorator(text) if callable(text) else decorator

@superLog
def supernName(s):
    print(s)
supernName('陈某人天才2')
print('my name now is:', supernName.__name__)


@superLog('hello')
def supernName(text):
    print(text)
supernName('陈某人天才2')