py_ver1 = 'python 2.7'
py_ver2 = 'python 3.11.2'

if py_ver1 == py_ver2:
    print('одинаковые версии')
    print('ещё одна операция в блоке')
print()

py_ver1_len = len(py_ver1)

if py_ver1_len == 8:
    print(py_ver1, 'версия ядра')
# зависимые блоки одной условной конструкции
elif py_ver1_len == 10 or py_ver1_len == 11:
    print(py_ver1, 'мажорная версия')
elif py_ver1_len == 12 or py_ver1_len == 13:
    print(py_ver1, 'минорная версия')

py_ver2_len = len(py_ver2)

if py_ver2_len == 8:
    print(py_ver2, 'версия ядра')
# независимые условные конструкции
if py_ver2_len == 10:
    print(py_ver2, 'мажорная версия') 
if py_ver2_len == 11:
    print(py_ver2, 'мажорная версия') 
if py_ver2_len == 12:
    print(py_ver2, 'минорная версия')    
if py_ver2_len == 13:
    print(py_ver2, 'минорная версия')    

