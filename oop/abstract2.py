from abc import ABCMeta, ABC, abstractmethod
from decimal import Decimal, Context


class Money(Decimal, metaclass=ABCMeta):
    def __new__(cls, value):
        return super().__new__(cls, f'{float(value):.2f}')
    
    @abstractmethod
    def __str__(self) -> str:
        pass


class RUB(Money):
    def __str__(self):
        return f'{super(Money, self).__str__()} ₽'


class USD(Money):
    def __str__(self):
        return f'${super(Money, self).__str__()}'


class Recipe(Money):
    def __str__(self):
        return f' + {super(Money, self).__str__()} ...'

