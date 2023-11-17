"""
Liskov Substituion Principle — Принцип Подстановки Лисков

Нижний уровень
"""


class Rectangle:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self.area = width * height
    
    @property
    def width(self) -> int:
        return self._width
    
    @width.setter
    def width(self, new_width: int) -> None:
        self._width = new_width
        self.area = new_width * self._height
    
    @property
    def height(self) -> int:
        return self._height
    
    @height.setter
    def height(self, new_height: int) -> None:
        self._height = new_height
        self.area = self._width * new_height


class Square(Rectangle):
    def __init__(self, side: int):
        self._width = side
        self._height = side
        self.area = side ** 2
    
    # нарушение LSP — в базовом классе изменение одного атрибута не влекло за собой изменения другого
    @Rectangle.width.setter
    def width(self, new_width: int) -> None:
        self._width = new_width
        self._height = new_width
        self.area = new_width ** 2
    
    # нарушение LSP — в базовом классе изменение одного атрибута не влекло за собой изменения другого
    @Rectangle.height.setter
    def height(self, new_height: int) -> None:
        self._width = new_height
        self._height = new_height
        self.area = new_height ** 2

