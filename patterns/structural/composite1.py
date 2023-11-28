"""Демонстратор простого компоновщика."""

from abc import ABC, abstractmethod
from dataclasses import dataclass


class VectorGraphicObject(ABC):
    @abstractmethod
    def render(self):
        pass


@dataclass
class Line(VectorGraphicObject):
    name: str
    length: float
    
    def render(self):
        print(f'{self.name}: {self.length}')


@dataclass
class Text(VectorGraphicObject):
    name: str
    text: str
    
    def render(self):
        print(self.text)


class Group(VectorGraphicObject):
    def __init__(self, name: str):
        self.name = name
        self.__elements: list[VectorGraphicObject] = []

    def add_elements(self, *args: VectorGraphicObject):
        self.__elements.extend(args)

    def render(self):
        for elem in self.__elements:
            elem.render()


# >>> ab = Line('AB', 2)
# >>> bc = Line('BC', 5)
# >>> cd = Line('CD', 2)
# >>> da = Line('DA', 5)
# >>> formula = Text('perimeter', 'P = AB + BC + CD + DA')

# >>> da.render()
# DA: 5
# >>> formula.render()
# P = AB + BC + CD + DA

# >>> figure = Group('perimeter_formula1')
# >>> figure.add_elements(ab, bc, formula, cd, da)
# >>> figure.render()
# AB: 2
# BC: 5
# P = AB + BC + CD + DA
# CD: 2
# DA: 5

