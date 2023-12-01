"""Демонстратор стратегии: функции в роли стратегий."""

from collections.abc import Callable
from numbers import Number
from operator import add, sub, floordiv, mul, truediv, pow


class Calculator:
    def __init__(self, number1: Number, number2: Number):
        self.number1 = number1
        self.number2 = number2
    
    def __eq__(self, other):
        if isinstance(other, Calculator):
            return self.number1 == other.number1 and self.number2 == other.number2
        else:
            raise TypeError
    
    def calculate(self, operation: Callable[[Number, Number], Number]) -> Number:
        """Метод-интерфейс для различных стратегий поведения — математических операций, выполняемых с числами number1 и number2.
        
        :param operation: вызываемый объект, принимающий на вход ровно два числа и возвращающий число
        """
        return operation(self.number1, self.number2)


c = Calculator(10, 3)

operations = (add, sub, mul, truediv, floordiv, pow)
for oper in operations:
    print(c.calculate(oper))
print()

# print(c.calculate(op.neg))
print(c.calculate(Calculator))
print(c.calculate(Calculator) == c)
