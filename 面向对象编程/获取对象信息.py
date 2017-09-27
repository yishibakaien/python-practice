
# 可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：

print(isinstance([1, 2, 3], (list, tuple)))

print(isinstance((1, 2, 3), (list, tuple)))

import sys

print(dir(sys))


# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()

def p(*args):
    print(*args)

p('hasattr(obj, "x")?', hasattr(obj, 'x'))

p('obj.x?', obj.x)

p('hasattr(obj, "y")?', hasattr(obj, 'y'))

setattr(obj, 'y', 19)

p('getattr(obj, "y")?', getattr(obj, 'y'))

p('obj.y?', obj.y)

# 如果试图获取不存在的属性，会抛出AttributeError的错误：

p('当获取不到值时，返回默认值(404) getattr(obj, "z", 404)?', getattr(obj, 'z', 404))
