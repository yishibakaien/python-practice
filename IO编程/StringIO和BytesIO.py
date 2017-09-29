
from io import StringIO

f = StringIO()

f.write('Hello')

f.write(' ')

f.write('World!')

with open('./test.txt', 'w', encoding = 'UTF-8') as file:
    file.write(f.getvalue())

f = StringIO('11\n22\n33')
while True:
    s = f.readline()
    # print('s', s)
    if s == '':
        break
    print(s.strip())