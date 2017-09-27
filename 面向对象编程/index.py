# 初步感受一下类 --- 面向对象的编程
# 一个Class既包含数据，又包含操作数据的方法
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

bart = Student('Bart Simpson', 59)

lisa = Student('Lisa Chen', 87)

bart.print_score()
lisa.print_score()