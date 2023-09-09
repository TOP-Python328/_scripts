from collections.abc import Iterable


data1 = [
    12,
    '345',
    (6, 7),
    {
        'a': 8,
        'b': 9,
        'c': 10
    },
    1.1,
    [
        (0.12, 0.13, 0.14),
        (0.15, 0.16, 0.17),
    ]
]
data2 = [
    'a',
    'b',
    ['c', 'd', 'e'],
    (
        {'f': 1, 'g': 2, 'h': 3},
        {'i': 1, 'j': 2, 'k': 3}
    ),
    'mn',
    'op',
    {
        'q': {
            'r': {10, 20, 30}
        },
        's': {
            't': {40, 50, 60}
        },
    }
]


def flatten(data: Iterable) -> list:
    """"""
    results = []
    for elem in data:
        if isinstance(elem, dict):
            results.extend(flatten(elem.values()))
        elif isinstance(elem, Iterable) and not isinstance(elem, str):
            results.extend(flatten(elem))
        else:
            results.append(elem)
    return results


# >>> flatten(data1)
# [12, '345', 6, 7, 8, 9, 10, 1.1, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17]
# >>> flatten(data2)
# ['a', 'b', 'c', 'd', 'e', 1, 2, 3, 1, 2, 3, 'mn', 'op', 10, 20, 30, 40, 50, 60]
