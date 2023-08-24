Iterable = str | range | tuple | list | set | frozenset | dict

def filter(func_obj: 'function', iterator: Iterable) -> list:
    """Приблизительный вариант реализации встроенной функции высшего порядка filter()."""
    results = []
    for elem in iterator:
        if func_obj(elem):
            results.append(elem)
    return results


# >>> words = ['там', 'на', 'идёт', '', 'лукоморье', '']
# >>>
# >>> filter(bool, words)
# ['там', 'на', 'идёт', 'лукоморье']


# >>> def is_positive(number) -> bool:
# ...     return number > 0
# ...
# >>> filter(is_positive, [1, -2, 0, 5, 12, -7, -1, 4])
# [1, 5, 12, 4]

