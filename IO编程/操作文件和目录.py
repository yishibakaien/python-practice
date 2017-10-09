import os
print(os.name) # nt => windows, posix => Linux、Unix 或 Mac OS X

# 1 操作系统中的环境变量
print(os.environ)

# 2 要获取某个环境变量的值，可以调用 os.environ.get('key') 
print('获取环境变量：', os.environ.get('PATH'))

# 3 操作文件和目录

# 3.1 查看当前目录的绝对路径
__dirname = os.path.abspath('.')
print(__dirname)

# 3.2 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
__target = os.path.join(__dirname, 'testdir')

# 3.3 然后创建一个目录
os.mkdir(__target)

# 3.4 删除掉一个目录
os.rmdir(__target)

## 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
## 拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数
#

# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。

# 查找单层
def fileFinder(s):
    _abspath = os.path.abspath('.')
    print([(x, os.path.join(_abspath, x)) for x in os.listdir('.') if os.path.isfile(x) and x.find(s) != -1])
fileFinder('test')

# 实现查找多层

def supperFileFinder(s, path = os.path.abspath('.')):
    files = os.listdir(path)
    for x in files:
        p = os.path.join(path, x)
        if os.path.isdir(x):
            supperFileFinder(s, p)
        if os.path.isfile(x) and x.find(s) != -1:
            print('找到符合目标的文件地址为：', p)

supperFileFinder('test')
print('===')
supperFileFinder('test', 'F:\_python_study\IO编程\subdir')