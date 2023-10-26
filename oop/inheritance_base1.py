from numbers import Real
from typing import Self


class Battery(int):
    def __new__(cls, capacity: int, charge: int = 0) -> Self:
        instance = super().__new__(cls, charge)
        instance.capacity = capacity
        return instance
    
    def __put_in_range(self, value: int) -> Self:
        if value < 0:
            return self.__class__(self.capacity)
        elif value > self.capacity:
            return self.__class__(self.capacity, self.capacity)
        else:
            return self.__class__(self.capacity, value)
    
    def __iadd__(self, level: Real):
        if isinstance(level, Real):
            # res = int.__add__(self, level)
            res = super().__add__(level)
            return self.__put_in_range(res)
        else:
            TypeError('...')
    
    def __add__(self, level: Real):
        return self.__iadd__(level)
    
    def __isub__(self, level: Real):
        if isinstance(level, Real):
            res = super().__sub__(level)
            return self.__put_in_range(res)
        else:
            TypeError('...')
    
    def __str__(self):
        return f'<{self.__class__.__name__}: {self!r}/{self.capacity}>'


# >>> crona = Battery(15)
# >>>
# >>> crona += 10
# >>> crona
# 10
# >>> type(crona)
# <class '__main__.Battery'>
# >>>
# >>> crona + 20
# 15
# >>> type(crona + 20)
# <class '__main__.Battery'>
# >>>
# >>> crona -= 3
# >>> crona
# 7
# >>> type(crona)
# <class '__main__.Battery'>
# >>>
# >>> crona -= 50
# >>> crona
# 0
# >>> type(crona)
# <class '__main__.Battery'>
