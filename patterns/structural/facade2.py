"""Демонстратор фасада."""

from abc import ABC, abstractmethod
from random import choice, shuffle


class Specie(ABC):
    name: str
    id: int = 0

    def __init__(self, alive: bool = True, reproducing: bool = False):
        self.alive = alive
        self.reproducing = reproducing

    def __hash__(self):
        return self.id + 1

    def __str__(self):
        return self.name

    @staticmethod
    @abstractmethod
    def action():
        pass

    @classmethod
    def reproduce(cls):
        return cls()


class Hawk(Specie):
    name: str = 'H'

    @staticmethod
    def action():
        return 'attack'


class Dove(Specie):
    name: str = 'D'

    @staticmethod
    def action():
        return 'defend'


def iterate(population: list[Specie]) -> list[Specie]:
    """Обеспечивает один шаг симуляции."""
    half = len(population) // 2
    part_left = population[:half]
    part_right = population[half:]
    
    for s1, s2 in zip(part_left, part_right):
        a1, a2 = s1.action(), s2.action()
        
        if a1 == 'attack':
            if a2 == 'attack':
                # два ястреба
                s1.alive = False
                s2.alive = False
            elif a2 == 'defend':
                # ястреб и голубь
                s2.alive = False
                s1.reproducing = True
        elif a1 == 'defend':
            if a2 == 'attack':
                # голубь и ястреб
                s1.alive = False
                s2.reproducing = True
            elif a2 == 'defend':
                choice((s1, s2)).reproducing = True
    
    population = []
    for specie in part_left + part_right:
        if specie.alive:
            population.append(specie)
            if specie.reproducing:
                population.append(specie.reproduce())
    
    return population


class Simulation:
    """
    Фасад для модели данных и управляющего кода среднего уровня.
    """
    def __init__(self, hawks: int, doves: int):
        self.population: list[Specie] = []
        for _ in range(hawks):
            self.population.append(Hawk())
        for _ in range(doves):
            self.population.append(Dove())
        shuffle(self.population)

    def show_animals(self):
        print(*map(str, self.population))

    def iterate(self) -> bool:
        self.population = iterate(self.population)
        shuffle(self.population)
        if len(self.population) in (0, 1):
            return False
        else:
            return True

    def until_deadend(self):
        self.show_animals()
        while self.iterate():
            self.show_animals()
            if len(set(self.population)) == 1:
                break


# >>> s1 = Simulation(4, 20)
# >>> s1.until_deadend()
