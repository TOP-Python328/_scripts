from typing import Self


class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def __eq__(self, other: Self):
        try:
            return {self.width, self.height} == {other.width, other.height}
        except AttributeError:
            try:
                return self.width == self.height == other.side
            except AttributeError:
                return False


rc1 = Rectangle(2, 3)
rc2 = Rectangle(2, 3)
rc3 = Rectangle(3, 2)
rc4 = Rectangle(4, 7)
rc5 = Rectangle(5, 5)

# до реализации методов сравнения
# >>> rc1 == rc2
# False
# >>>
# >>> id(rc1)
# 2111987977040
# >>> id(rc2)
# 2111987977168

# после реализации методов сравнения
# >>> rc1 == rc2
# True
# >>> rc1 == rc3
# True
# >>> rc1 == rc4
# False
# >>> rc1 == (2, 3)
# False


class Square:
    def __init__(self, side: float):
        self.side = side


sq1 = Square(5)

# >>> rc5 == sq1
# True
# >>> sq1 == rc5
# True
