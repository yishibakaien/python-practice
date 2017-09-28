
# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：
# 

class Student(object):
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100')
        self._score = value

# Python 内置的 @property 装饰器就是负责把一个方法变成属性调用

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        
        if value < 0 or value > 100:
            raise ValueError('score must be between 0 ~ 100')
        self._score = value

s = Student()
s.score = 60
print(s.score) # 60
# s.score = 9999 # 报错 ValueError: score must be between 0 ~ 100


## 通过 @property 可以实现只读属性(只设置 getter 不设置 setter)
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2017 - self.birth

a = Student()

a.birth = 2004

print('a 的年龄是:', a.age)

# a.age = 18  报错 AttributeError: can't set attribute


## 练习 请利用 @property 给一个 Screen 对象加上 width 和 height 属性，以及一个只读属性 resolution

class Screen(object):
    # __slots__ = ('width', 'height')

    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._height * self._width

s = Screen()

# print('Screen 实例 s', s)
# print('未设置 s.width 时：', s.width)

s.width = 1440
print('实例s 的 width', s.width)

s.height = 980
print('实例s 的 height', s.height)

assert s.resolution == 1411200, '1440 * 980 = %d ?' % s.resolution
print('实例s 的 resolution', s.resolution)

# s.resolution = 150000 # 报错 AttributeError: can't set attribute

class Screen2(object):

    def width(self, value):
        self.width = value

    def height(self, value):
        self.height = value

    @property
    def resolution(self):
        return self.height * self.width

s2 = Screen2()

print('未设置 s2.width 时：', s2.width)

s2.width = 1440
s2.height = 980

print('s2.resolution:', s2.resolution)
# s2.resolution = 12345
