"""
Dependencies Inversion Principle — Принцип Инверсии Зависимостей

Нижний уровень
"""

from collections.abc import Generator
from dataclasses import dataclass
from enum import Enum
from typing import Self


@dataclass
class Person:
    name: str
    
    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other: Self):
        if isinstance(other, self.__class__):
            return self.name == other.name
        else:
            raise TypeError
    
    def __repr__(self):
        return self.name


class Relation(Enum):
    PARENT = 0
    CHILD = 1


class Relationship:
    def __init__(self):
        self.storage: set[tuple[Person, Relation, Person]] = set()
    
    def add_relation(
            self,
            parent: Person,
            child: Person
    ) -> None:
        self.storage.add((parent, Relation.PARENT, child))
        self.storage.add((child, Relation.CHILD, parent))
    
    # нарушение DIP — не предоставлен интерфейс, код верхнего уровня вынужден использовать детали конкретной реализации
    
    # решение — предоставить интерфейс для кода верхнего уровня
    def find_all_children(self, person: Person) -> Generator[Person]:
        for person1, relation, person2 in self.storage:
            if person == person1:
                if relation is Relation.PARENT:
                    yield person2

