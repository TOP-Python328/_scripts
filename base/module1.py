"""
Точка входа.
"""

print('начало выполнения главного модуля')

import module2

print('окончание выполнения главного модуля')


# >>> type(module2)
# <class 'module'>
# >>>
# >>> module2
# <module 'module2' from 'D:\\G-Doc\\TOP Academy\\Python web\\328\\scripts\\base\\module2.py'>
# >>>
# >>> module2.__name__
# 'module2'
# >>>
# >>> module2.__doc__
# '\nДополнительный модуль 2.\n'
# >>>
# >>> module2.words
# ['additional', 'module', '2']


# >>> module2.module3
# <module 'module3' from 'D:\\G-Doc\\TOP Academy\\Python web\\328\\scripts\\base\\module3.py'>
# >>>
# >>> module2.module3.__name__
# 'module3'
# >>> module2.module3.__doc__
# '\nДополнительный модуль 3.\n'
# >>>
# >>> module2.module3.percent
# 0.05


# >>> module2.module3.percent = 0.12
# >>> module2.module3.percent
# 0.12


# >>> from module4 import product
# начало выполнения дополнительного модуля 4
# окончание выполнения дополнительного модуля 4
# >>>
# >>> from module4 import numbers
# >>>
# >>> numbers.append(8)
# >>>
# >>> from sys import modules
# >>>
# >>> modules['module4'].numbers
# [4, 9, 1, 3, 5, 8]
# >>>
# >>> numbers = 234
# >>>
# >>> modules['module4'].numbers
# [4, 9, 1, 3, 5, 8]
