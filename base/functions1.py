# объявление функции
def test_function():
    print('функция test_function вызвана')
    print(10**6)


# вызов функции
a = test_function()
b = test_function()

# функция test_function вызвана
# 1000000
# функция test_function вызвана
# 1000000
# >>> 
# >>> type(a)
# <class 'NoneType'>
# >>>
# >>> id(a)
# 140726954126536
# >>> id(b)
# 140726954126536
# >>>
# >>> a is b
# True
# >>>
# >>> c = print()

# >>> type(c)
# <class 'NoneType'>
# >>>
# >>> [test_function(), test_function()]
# функция test_function вызвана
# 1000000
# функция test_function вызвана
# 1000000
# [None, None]
