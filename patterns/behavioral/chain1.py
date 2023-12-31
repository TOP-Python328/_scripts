"""Демонстратор цепочки ответственности: цепочка методов."""

from dataclasses import dataclass
from typing import Optional, Self


@dataclass
class Creature:
    name: str
    attack: int
    defense: int
    
    def __str__(self):
        return f'{self.name}: A={self.attack} / D={self.defense}'


class CreatureModifier:
    """Базовый класс модификаторов, являющийся корневым элементом цепочки модификаторов и предоставляющий методы для прохождения по всем элементам цепочки."""
    def __init__(self, creature: Creature):
        self.creature = creature
        self.previous_modifier: Optional[CreatureModifier] = None
        self.next_modifier: Optional[CreatureModifier] = None
    
    def add_modifier(self, modifier: Self):
        """Формирует звено цепочки."""
        if self.next_modifier is None:
            modifier.previous_modifier = self
            self.next_modifier = modifier
        else:
            self.next_modifier.add_modifier(modifier)
    
    def clear(self):
        if self.next_modifier:
            return self.next_modifier.clear()
        else:
            self.undo()
    
    def undo(self):
        self.next_modifier = None
        if self.previous_modifier:
            self.previous_modifier.undo()
        self.previous_modifier = None
    
    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()


class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        self.creature.attack *= 2
        super().handle()
    
    def undo(self):
        self.creature.attack //= 2
        super().undo()


class IncreaseDefenseModifier(CreatureModifier):
    def handle(self):
        if self.creature.attack < 3*self.creature.defense:
            self.creature.defense += 1
        super().handle()
    
    def undo(self):
        if self.creature.attack <= 3*self.creature.defense:
            self.creature.defense -= 1
        super().undo()


goblin = Creature('Гоблин', 1, 1)
print('\nШёл грустный и голый гоблин по лесу')
print(goblin)

root = CreatureModifier(goblin)

mod1 = DoubleAttackModifier(goblin)
root.add_modifier(mod1)

mod2 = IncreaseDefenseModifier(goblin)
root.add_modifier(mod2)

root.handle()
print('\nВ лесу гоблин нашёл крепкую длинную палку, которой так удобно бить по головам врагов. А ещё на ветке висела чья-то старая хламида.')
print(goblin)

root.clear()
print('\nНа гоблина внезапно напал Серый Волк, порвал на лоскутки старую хламиду, отнял палку и убежал.')
print(goblin)

root.add_modifier(DoubleAttackModifier(goblin))

root.handle()
print('\nПод скалой гоблин нашёл небольшой камень, который так удобно лёг в гоблинячью руку.')
print(goblin)
