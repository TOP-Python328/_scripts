"""Open-Close Principle — Принцип Открытости-Закрытости"""

from abc import ABC, abstractmethod
from collections.abc import Iterable, Generator
from dataclasses import dataclass
from enum import Enum


class Color(Enum):
    GREEN = 'зелёный'
    BLUE = 'синий'
    RED = 'красный'


class Size(Enum):
    SMALL = 'маленький'
    MEDIUM = 'средний'
    LARGE = 'большой'


@dataclass
class Product:
    name: str
    color: Color
    size: Size
    
    def __str__(self):
        return f'{self.name} {self.color.value} {self.size.value}'


class ProductBase:
    def __init__(self, products: Iterable[Product]):
        self.products = products
    
    # нарушение OCP
    def by_color(self, color: Color) -> Generator[Product]:
        for prod in self.products:
            if prod.color is color:
                yield prod
    
    # нарушение OCP
    def by_size(self, size: Size) -> Generator[Product]:
        for prod in self.products:
            if prod.size is size:
                yield prod
    
    # нарушение OCP
    def by_color_and_size(self, color: Color, size: Size) -> Generator[Product]:
        for prod in self.products:
            if prod.color is color and prod.size is size:
                yield prod

# класс ProductBase нарушает OCP
# количество методов для фильтрации будет экспоненциально возрастать с увеличением количества критериев
# a b: a b ab
# a b c: a b c ab bc ac abc
# a b c d: a b c d ab bc cd ac ad bd abc abd bcd abcd


# решение — реализовать цепочку классов для критериев и комбинаций с использованием абстракции и наследования

class Criteria(ABC):
    @abstractmethod
    def match(self, product: Product) -> bool:
        pass


@dataclass
class ColorCriteria(Criteria):
    color: Color
    
    def match(self, product: Product) -> bool:
        return self.color is product.color


@dataclass
class SizeCriteria(Criteria):
    size: Size
    
    def match(self, product: Product) -> bool:
        return self.size is product.size


class AndCriteria(Criteria):
    def __init__(self, *criterias: Criteria):
        self.criterias = criterias
    
    def match(self, product: Product) -> bool:
        return all(map(
            lambda crit: crit.match(product),
            self.criterias
        ))


class ProductBase:
    def __init__(self, products: Iterable[Product]):
        self.products = products
    
    def filter(self, criteria: Criteria) -> Generator[Product]:
        for prod in self.products:
            if criteria.match(prod):
                yield prod


products = (
    Product('яблоко', Color.GREEN, Size.SMALL),
    Product('ель', Color.GREEN, Size.LARGE),
    Product('пожарная машина', Color.RED, Size.LARGE),
    Product('комбинезон', Color.BLUE, Size.MEDIUM),
    Product('пингвин', Color.BLUE, Size.SMALL),
    Product('гидрант', Color.RED, Size.MEDIUM),
)

# >>> pb = ProductBase(products)
# >>> 
# >>> crit_green = ColorCriteria(Color.GREEN)
# >>> crit_blue = ColorCriteria(Color.BLUE)
# >>> crit_red = ColorCriteria(Color.RED)
# >>> 
# >>> crit_small = SizeCriteria(Size.SMALL)
# >>> crit_med = SizeCriteria(Size.MEDIUM)
# >>> crit_large = SizeCriteria(Size.LARGE)
# >>> 
# >>> crit_green_and_large = AndCriteria(crit_green, crit_large)
# >>> 
# >>> print(*pb.filter(crit_green), sep='\n')
# яблоко зелёный маленький
# ель зелёный большой
# >>> 
# >>> print(*pb.filter(crit_med), sep='\n')
# комбинезон синий средний
# гидрант красный средний
# >>> 
# >>> print(*pb.filter(crit_green_and_large), sep='\n')
# ель зелёный большой

