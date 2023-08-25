def test_generator() -> 'generator':
    print('начало выполнения тела генераторной функции')
    print('первый шаг')
    yield 1
    print('второй шаг')
    yield -1
    print('третий шаг')
    yield 2
    print('четвёртый шаг')
    yield -2
    print('окончание выполнения тела генераторной функции')


# >>> gen_obj = test_generator()
# >>>
# >>> type(gen_obj)
# <class 'generator'>
# >>> 
# >>> gen_obj
# <generator object test_generator at 0x000001DD83D95A80>
# >>>
# >>> gen_obj.__next__()
# начало выполнения тела генераторной функции
# первый шаг
# 1
# >>> gen_obj.__next__()
# второй шаг
# -1
# >>> gen_obj.__next__()
# третий шаг
# 2
# >>> gen_obj.__next__()
# четвёртый шаг
# -2
# >>> gen_obj.__next__()
# окончание выполнения тела генераторной функции
# ...
# StopIteration
# >>> gen_obj.__next__()
# ...
# StopIteration
# по одному объекту генератора можно проитерироваться только один раз


# >>> gen_obj = test_generator()
# >>>
# >>> for n in gen_obj:
# ...     print(n, end=' ')
# ...
# начало выполнения тела генераторной функции
# первый шаг
# 1 второй шаг
# -1 третий шаг
# 2 четвёртый шаг
# -2 окончание выполнения тела генераторной функции


