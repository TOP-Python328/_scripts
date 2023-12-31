"""Демонстратор цепочки ответственности: брокер событий."""

# брокер событий - event broker
# диспетчер запросов - CQS (command and query selector)

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class Parameter(Enum):
    ATTACK = 0
    DEFENSE = 1


class Modifiers(list):
    """Вызываемый список методов handle() модификаторов."""
    def __call__(self, *args, **kwargs):
        for function in self:
            function(*args, **kwargs)
        # для отладчика
        pass


@dataclass
class Query:
    """Запрос, в котором вычисляются модифицируемые значения."""
    creature: 'Creature'
    parameter: Parameter
    value: int


class Game:
    """Брокер событий."""
    def __init__(self):
        self.modifiers = Modifiers()
    
    def calc_modified_value(
            self,
            sender: 'Creature',
            query: Query
    ) -> None:
        self.modifiers(sender, query)
        # для отладчика
        pass


@dataclass
class Creature:
    game: 'Game'
    name: str
    initial_attack: int
    initial_defense: int
    
    @property
    def attack(self) -> int:
        q = Query(self, Parameter.ATTACK, self.initial_attack)
        # выполнение конкретного запроса — это вычисление модифицируемого атрибута существа
        self.game.calc_modified_value(self, q)
        return q.value
    
    @property
    def defense(self) -> int:
        q = Query(self, Parameter.DEFENSE, self.initial_defense)
        self.game.calc_modified_value(self, q)
        return q.value
    
    def __str__(self):
        return f'{self.name}: A={self.attack} / D={self.defense}'


class CreatureModifier(ABC):
    def __init__(self, game: Game, creature: Creature):
        self.game = game
        self.creature = creature
        # во время инициализации объекта модификатора его объект метода handle добавляется в список обработчиков
        self.game.modifiers.append(self.handle)
        # для отладчика
        pass
    
    @abstractmethod
    def handle(self, sender: Creature, query: Query) -> None:
        pass
    
    def remove(self) -> None:
        self.game.modifiers.remove(self.handle)
        # для отладчика
        pass
    
    # для входа в блок with
    def __enter__(self):
        return self
    
    # для выхода из блока with
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.game.modifiers.remove(self.handle)


class DoubleAttackModifier(CreatureModifier):
    def handle(self, sender: Creature, query: Query) -> None:
        if self.creature is sender:
            if query.parameter is Parameter.ATTACK:
                query.value *= 2
        # для отладчика
        pass


class IncreaseDefenseModifier(CreatureModifier):
    def handle(self, sender: Creature, query: Query) -> None:
        if self.creature is sender:
            if query.parameter is Parameter.DEFENSE:
                if self.creature.attack <= 3 * query.value:
                    query.value += 1
        # для отладчика
        pass



new_game = Game()
goblin = Creature(new_game, 'Гоблин-воин', 3, 2)
print(goblin)

dam = DoubleAttackModifier(new_game, goblin)
print(goblin)

idm = IncreaseDefenseModifier(new_game, goblin)
print(goblin)

dam.remove()
print(goblin)

with DoubleAttackModifier(new_game, goblin):
    print(goblin)

print(goblin)
