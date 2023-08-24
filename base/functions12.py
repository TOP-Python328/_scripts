def test_func(arg1, arg2: str = '') -> None:
    """Документация"""


# >>> test_func
# <function test_func at 0x00000204178C4720>
# >>>
# >>> type(test_func)
# <class 'function'>
# >>>
# >>> test_func.__name__
# 'test_func'
# >>>
# >>> test_func.__annotations__
# {'arg2': <class 'str'>, 'return': None}
# >>>
# >>> test_func.__defaults__
# ('',)
# >>>
# >>> test_func.__doc__
# 'Документация'

