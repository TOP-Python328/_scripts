from collections.abc import Iterable
from functools import singledispatch
from math import pi
from random import randrange as rr, sample, uniform
from string import ascii_letters


@singledispatch
def data_insert(element):
    return None

@data_insert.register
def _(element: bool) -> bool:
    return bool(rr(2))

@data_insert.register
def _(element: int) -> int:
    return rr(-9, 10)

@data_insert.register
def _(element: float) -> float:
    return uniform(-pi, pi)

@data_insert.register
def _(element: str) -> str:
    return ''.join(sample(ascii_letters, k=rr(3, 9)))

@data_insert.register
def _(element: dict) -> dict:
    return {
        key: data_insert(elem)
        for key, elem in element.items()
    }

# @data_insert.register
# def _(element: Iterable) -> Iterable:
#     return element.__class__(
#         data_insert(elem)
#         for elem in element
#     )

@data_insert.register
def _(element: list) -> list:
    return [
        data_insert(elem)
        for elem in element
    ]

# @data_insert.register
# def _(element: range) -> range:
#     return range(
#         data_insert(element.start), 
#         data_insert(element.stop), 
#         data_insert(element.step)
#     )


# >>> data_insert('')
# 'kJOh'
# >>>
# >>> data_insert(0)
# -9
# >>>
# >>> data_insert(.0)
# 2.917410601493871
# >>>
# >>> data_insert([1, 2, ''])
# [-4, -7, 'wqvPc']
# >>>
# >>> data_insert({'a': 0, 'b': .0, 'c': (0, 0), 'd': {0, 1, ''}, 'e': 1+1j})
# {'a': -4, 'b': 0.4167611566746765, 'c': (-2, -5), 'd': {8, 'dEY', 4}, 'e': False}
# >>>
# >>> data_insert(range(9))
# range(1, 5, -9)

