from pytest import mark

from random import randrange


def test_first():
    print('первый тест')
    assert True


def test_second():
    print('второй тест')
    assert False


def test_third():
    assert randrange(-1, 2) in range(-1, 2)


def test_fourth():
    n1 = 1 / 0
    assert n1


@mark.xfail
def test_fifth():
    assert False


@mark.xfail
def test_sixth():
    assert True

