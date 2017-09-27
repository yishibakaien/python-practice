
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

bart = Student('Bart Simpson', 59)

bart.print_score() # 59

# 此时从代码的外部可以自由的修改属性

bart.score = 95

bart.print_score() #95

# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问：
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    
    def print_score(self):
        print('%s2: %s' % (self.__name, self.__score))

lisa = Student('Lisa Simpson', 59);

lisa.print_score() # 59

lisa.__score = 95
lisa.print_score() # 59

# print(lisa.score) # AttributeError: 'Student' object has no attribute 'score'
# 但是实际上 这个 "__score" 被 python 解释器编译为 _Student__score 了
print('lisa._Student__score', lisa._Student__score)

# 如果要修改或获得内部的属性，可以通过定义内部方法实现
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    
    def print_message(self):
        print('%s3: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name
    def set_score(self, score):
        self.__score = score

mike = Student('Mike kayle', 59);

mike.print_message() # Mike kayle3: 59

print(mike.get_name()) # Mike kayle3 

mike.set_score(100)

mike.print_message() # Mike kayle3: 100
