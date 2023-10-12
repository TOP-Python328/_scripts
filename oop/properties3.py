from functools import cache
from typing import Literal


str_formats = Literal['fio', 'io', 'initials_first', 'initials_least']


class Person:
    default_str_format: str_formats = 'io'
    
    def __init__(self, last_name: str, first_name: str, patr_name: str):
        self.last_name = last_name
        self.first_name = first_name
        self.patr_name = patr_name
    
    def __hash__(self):
        return hash((self.last_name, self.first_name, self.patr_name))
    
    @property
    @cache
    def fio(self) -> str:
        print('вызов')
        return f'{self.last_name} {self.first_name} {self.patr_name}'
    
    @property
    @cache
    def io(self) -> str:
        print('вызов')
        return f'{self.first_name} {self.patr_name}'
    
    @property
    @cache
    def initials_first(self) -> str:
        print('вызов')
        return f'{self.first_name[0]}. {self.patr_name[0]}. {self.last_name}'
    
    @property
    @cache
    def initials_least(self) -> str:
        print('вызов')
        return f'{self.last_name} {self.first_name[0]}. {self.patr_name[0]}.'
    
    def __repr__(self):
        return getattr(self, self.default_str_format)


ivan = Person('Разумов', 'Иван', 'Олегович')


# >>> ivan.__hash__()
# -5360312657123988596
# >>>
# >>> ivan
# вызов
# Иван Олегович
# >>> ivan
# Иван Олегович
# >>>
# >>> ivan.first_name = 'Иоанн'
# >>>
# >>> ivan.__hash__()
# -7297448345556309119
# >>>
# >>> ivan
# вызов
# Иоанн Олегович
# >>> ivan
# Иоанн Олегович

