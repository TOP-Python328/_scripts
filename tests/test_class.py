from pathlib import Path
from sys import path

path.append(r'c:\Users\Геннадий\Documents\_TOP\328\scripts\oop')

import methods3


class TestCat:
    
    cat = methods3.Cat()
    journal = Path(path[0]) / 'test_class.log'
    
    def log(self, data) -> None:
        with open(self.journal, 'a', encoding='utf-8') as out:
            print(data, file=out)
    
    def test_meow(self):
        self.log(f'test_meow: {id(self.cat) = }')
        assert len(self.cat.meow()) == 3
    
    def test_hungry(self):
        self.log(f'test_hungry: {id(self.cat) = }')
        assert 7 <= len(self.cat.hungry()) <= 15
    
    def test_reproduce_count(self):
        self.log(f'test_reproduce_count: {id(self.cat) = }')
        assert 2 <= len(self.cat.reproduce()) <= 4
    
    def test_reproduce_type(self):
        self.log(f'test_reproduce_type: {id(self.cat) = }')
        assert all(map(
            lambda kitten: isinstance(kitten, methods3.Cat),
            self.cat.reproduce()
        ))

