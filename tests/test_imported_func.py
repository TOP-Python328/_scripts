from pytest import mark

from sys import path

path.append(r'c:\Users\Геннадий\Documents\_TOP\328\scripts\base')

import functions4


data = (
    (1, 1, '+', 2),
    (1, 1, '-', 0),
    (2, 2, '*', 4),
    (2, 2, '/', 1),
    (3, 0, '/', float('inf')),
)


@mark.parametrize('n1,n2,op,res', data)
def test_calculator(n1: int, n2: int, op: str, res: float):
    breakpoint()
    assert functions4.calculator(n1, n2, op) == res
