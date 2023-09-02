"""
Дополнительный модуль 4.
"""

print('начало выполнения дополнительного модуля 4')


def product(*numbers):
    result = 1
    for n in numbers:
        result *= n
    return result


numbers = [4, 9, 1, 3, 5]

print('окончание выполнения дополнительного модуля 4')
