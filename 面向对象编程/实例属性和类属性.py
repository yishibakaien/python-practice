
# 由于Python是动态语言，根据类创建的实例可以任意绑定属性。
# 给实例绑定属性的方法是通过实例变量，或者通过self变量：
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90

class Animal(object):
    name = 'Animal'

a = Animal()

print(a.name) # Animal

print(Animal.name) # Animal

a.name = 'myName'

print(a.name) # myName

print(Animal.name) # Animal

del a.name # 删除掉 s 实例上的 name 属性

print(a.name) # Animal