# сохранение объектов анонимных функций в переменные категорически не рекомендуется!
func1 = lambda: 'вызов анонимной функции'
func2 = lambda num1, num2: num1 * num2

# >>> func1
# <function <lambda> at 0x0000016430934720>
# >>> func1.__name__
# '<lambda>'
# >>>
# >>> func2
# <function <lambda> at 0x0000016430C62CA0>
# >>> func2.__name__
# '<lambda>'
# >>>
# >>> type(func1)
# <class 'function'>

print(*filter(
    lambda n: n < 0, 
    map(int, input('числа > ').split())
))

# числа > 2 -1 13 7 -9 3
# -1 -9
