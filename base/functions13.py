# дженерик — используется только для аннотаций
Iterable = str | range | tuple | list | set | frozenset | dict

def map(function: 'function', iterator: Iterable) -> list:
    """Упрощённый вариант реализации встроенной функции высшего порядка map()."""
    results = []
    for elem in iterator:
        results.append(function(elem))
    return results


# >>> numbers = [0.079, 1.127, -2.9, 1.81]
# >>>
# >>> map(round, numbers)
# [0, 1, -3, 2]
# >>>
# >>> map(int, '192031')
# [1, 9, 2, 0, 3, 1]
# >>>
# >>> map(pow, numbers)
# ... 
# TypeError: pow() missing required argument 'exp' (pos 2)


def map(
        function: 'function', 
        iterator: Iterable,
        *iterators: Iterable,
) -> list:
    """Приблизительный вариант реализации встроенной функции высшего порядка map()."""
    # iterators = (iterator, ) + iterators
    iterators = iterator, *iterators
    results = []
    for args in zip(*iterators):
        results.append(function(*args))
    return results


# >>> map(pow, [10, 3, 2.2], [3, 10, 2])
# [1000, 59049, 4.840000000000001]

