from pytest import fixture

from pathlib import Path
from sys import path

path.append(r'c:\Users\Геннадий\Documents\_TOP\328\scripts\oop')
journal = Path(path[0]) / 'test_fixtures.log'

import methods3


@fixture
def new_cat() -> methods3.Cat:
    return methods3.Cat()


def log(data) -> None:
    with open(journal, 'a', encoding='utf-8') as out:
        print(data, file=out)


def test_meow(new_cat):
    log(f'test_meow: {id(new_cat) = }')
    assert len(new_cat.meow()) == 3


def test_hungry(new_cat):
    log(f'test_hungry: {id(new_cat) = }')
    assert 7 <= len(new_cat.hungry()) <= 15


def test_reproduce_count(new_cat):
    log(f'test_reproduce_count: {id(new_cat) = }')
    assert 2 <= len(new_cat.reproduce()) <= 4

def test_reproduce_type(new_cat):
    log(f'test_reproduce_type: {id(new_cat) = }')
    assert all(map(
        lambda kitten: isinstance(kitten, methods3.Cat),
        new_cat.reproduce()
    ))

