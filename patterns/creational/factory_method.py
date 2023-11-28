"""Демонстратор фабричного метода."""

from enum import Enum
from math import cos, sin
from typing import Self


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    # не оптимальный вариант
    # def __init__(
    #         self,
    #         a: float,
    #         b: float,
    #         system: CoordinateSystem = CoordinateSystem.CARTESIAN
    # ):
    #     if system is CoordinateSystem.CARTESIAN:
    #         self.x = a
    #         self.y = b
    #     elif system is CoordinateSystem.POLAR:
    #         self.x = a * cos(b)
    #         self.y = a * sin(b)
    
    # оптимальный вариант
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    @classmethod
    def cartesian(cls, x: float, y: float) -> Self:
        """Создаёт объект точки, заданной декартовыми координатами.

        :param x: координата оси абсцисс
        :param y: координата оси ординат
        """
        return cls(float(x), float(y))
    
    @classmethod
    def polar(cls, rho: float, phi: float) -> Self:
        """Создаёт объект точки, заданной полярными координатами.

        :param rho: (ρ) радиальная компонента
        :param phi: (φ) азимут (в радианах)
        """
        x = rho * cos(phi)
        y = rho * sin(phi)
        return cls(x, y)
    
    def __repr__(self):
        return f"<{self.__class__.__name__}: x={self.x}, y={self.y}>"
    
    def __str__(self):
        return f"({self.x}; {self.y})"


# >>> Point(0, 0)
# <Point: x=0, y=0>

# >>> Point(1, 3)
# <Point: x=1, y=3>

# >>> Point.polar(4, 0.5)
# <Point: x=3.510330247561491, y=1.917702154416812>

# >>> Point.cartesian(6, 10)
# <Point: x=6, y=10>

