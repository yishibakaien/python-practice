
# 当子类需要继承 多种 父类的功能时，需要多重继承
# 

# Dog - 狗狗；
# Bat - 蝙蝠；
# Parrot - 鹦鹉；
# Ostrich - 鸵鸟；
# 
# 可有以下几种分法
# 
# 1、哺乳动物 -- 鸟类
# 2、是否会飞
# 3、哺乳类 - 只能跑的哺乳类，能飞的哺乳类
# 4、鸟类 - 只能跑的鸟类， 能飞的鸟类
# .... 有非常多种分法，层次会非常复杂，所有要通过多重继承来 简化
# 


class Animal(object):
    pass

## 先按照大类来区分
# 哺乳类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

# 现在，我们要给动物再加上 Runnable 和Flyable 的功能，只需要先定义好 Runnable 和 Flyable 的类：
class Runable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

# 对于需要Runnable功能的动物，就多继承一个Runnable，例如Dog
class Dog(Mammal, Runnable):
    pass

# 对于需要Flyable功能的动物，就多继承一个Flyable，例如Bat
class Bat(Mammal, Flyable):
    pass

# class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
#     pass


