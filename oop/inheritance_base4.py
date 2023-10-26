from math import floor, ceil

# storage = DictOfRanges({
#     (1, 10): 'мало',
#     (11, 70): 'нормально',
#     (71, 100): 'много'
# })
# storage[5] --> 'мало'
# storage[(1, 10)] --> 'мало'


class DictOfRanges(dict):
    def __init__(self, mappable: dict):
        for key in mappable:
            if (
                   not isinstance(key, tuple) 
                or len(key) != 2
                or not isinstance(key[0], int) 
                or not isinstance(key[1], int)
            ):
                raise ValueError('...')
        super().__init__(mappable)
    
    def __getitem__(self, key):
        if isinstance(key, int):
            for left, right in self:
                if left <= key <= right:
                    return super().__getitem__((left, right))
        else:
            return super().__getitem__(key)


class Hero:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health: int = health
        self.__status: DictOfRanges = DictOfRanges({
            (0, floor(0.101*health)): 'при смерти',
            (ceil(0.101*health), floor(0.401*health)): 'тяжело ранен',
            (ceil(0.401*health), floor(0.801*health)): 'ранен',
            (ceil(0.801*health), health): 'здоров',
        })
    
    def __repr__(self):
        return f'{self.name}: {self.__status[self.health]}'



# >>> ilya = Hero('Илья-Муромец', 150)
# >>> ilya
# Илья-Муромец: здоров
# >>>
# >>> ilya._Hero__status
# {(0, 15): 'при смерти', (16, 60): 'тяжело ранен', (61, 120): 'ранен', (121, 150): 'здоров'}
# >>>
# >>> ilya.health -= 100
# >>> ilya
# Илья-Муромец: тяжело ранен

