
try:
    print('try...')
    # r = 10 / 0
    a = 'a'
    # int(a)
    # print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
except ValueError as e:
    print('ValueError:', e)
else:
    print('success')
finally:
    print('finally...')
print('END')