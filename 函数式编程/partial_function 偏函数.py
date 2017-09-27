
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。 

import functools

# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
int2 = functools.partial(int, base = 2)

print(int2('10010')) # 18

max2 = functools.partial(max, 10)

print(max2(5, 6, 7)) # 10 
print(max2(8, 10, 15)) # 15