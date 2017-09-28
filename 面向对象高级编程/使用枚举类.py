
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

for name, member in Weekday.__members__.items():
    print(name, '=>', member)


# http://www.cnblogs.com/ucos/p/5896861.html  接下来是更清晰的枚举类讲解

from enum import Enum, unique

# 如果要限制定义枚举时，不能定义相同值的成员。可以使用装饰器@unique【要导入unique模块】
@unique
class Color(Enum):
    red = 1
    orange = 2
    yellow = 3
    green = 4
    blue = 5
    indigo = 6
    purple = 7

# 如果枚举中存在相同值的成员，在通过值获取枚举成员时，只能获取到第一个成员
class Color2(Enum):
    red = 1
    red_alias = 1

print('Color2(1)', Color2(1)) # Color2.red


# 枚举取值
# 1 通过成员的名称来取值
print('Color["red"]', Color['red']) # Color.red

# 2 通过成员的值来获取成员
print('Color(2)', Color(2)) # Color.orange

# 3 通过成员，来获取它的名称和值
red_rember = Color.red

print('red_rember.name', red_rember.name) # red

print('red_rember.value', red_rember.value) # 1

# 枚举支持迭代器

for color in Color:
    print(color, color.value)

# 如果枚举有值重复的成员，循环遍历枚举时只获取值重复成员的第一个成员
class Color3(Enum):
    red = 1
    orange = 2
    yellow = 3
    red_alias = 1

for color in Color3: # 输出结果是：Color3.red、Color3.orange、Color3.yellow
    print(color)


# 如果想把值重复的成员也遍历出来，要用枚举的一个特殊属性__members__
class Color4(Enum):
    red = 1
    orange = 2
    yellow = 3
    red_alias = 1

for color in Color4.__members__.items(): 
    print(color)
# 输出结果：('red', <Color4.red: 1>)、('orange', <Color4.orange: 2>)、('yellow', <Color4.yellow: 3>)、('red_alias', <Color4.red: 1>)


# 枚举成员可进行同一性比较
print('Color.red is Color.red', Color.red is Color.red) # True

print('Color.red is not Color.blue', Color.red is not Color.blue) # True

# 枚举成员可进等值比较
print('Color.blue == Color.red', Color.blue == Color.red) # False

print('Color.blue != Color.red', Color.blue != Color.red) # True

# 枚举成员不能进行大小比较
## print('Color.red < Color.blue', Color.red < Color.blue) # 会报错
