
## __slots__ 主要用于限制实例只能添加某些属性

class Student(object):
    pass

s = Student()
s.name = 'cloud'
print(s.name) # cloud


# 定义一个函数作为实例方法
def set_age(self, age): 
    self.age = age

from types import MethodType

s.set_age = MethodType(set_age, s) # 给实例绑定一个方法

s.set_age(25) # 调用实例方法

print(s.age) # 25


# 在 Student Class 上绑定方法后，所有的实例均可调用
def set_score(self, score):
    self.score = score

Student.set_score = set_score

s.set_score(100)

print(s.score) # 100

# 使用 __slots__
# 用于限制实例的属性，比如，只允许对Student实例添加name和age属性。
class Student(object):
    __slots__ = ('name', 'age') # 用 tuple 定义绑定的属性名称

s = Student()
s.name = 'cloud'
s.age = '24'
s.score = '99' # 这里会报错 AttributeError: 'Student' object has no attribute 'score'
