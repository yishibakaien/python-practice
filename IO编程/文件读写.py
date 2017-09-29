
f = open('./test.txt', 'r', encoding = 'utf-8')
a = f.read()
f.close()
print(a)

with open('./test.txt', 'r', encoding = 'utf-8') as f:
    print(f.read())

with open('./test.txt', 'r', encoding = 'utf-8') as f:
    for line in f.readlines():
        print(line.strip()) # 把末尾的 '\n' 去掉

with open('./test.jpg', 'rb') as f:
    print(len(f.read()))

# 写文件
with open('test.txt', 'w', encoding = 'utf-8') as f:
    f.write('天才就是我，我就是天才')