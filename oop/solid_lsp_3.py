"""Liskov Substituion Principle — Принцип Подстановки Лисков"""

from numbers import Number
from typing import Any


class DictOfRanges(dict):
    """
    Словарь диапазонов: при использовании объекта Number в качестве ключа возвращает значение, соответствующее кортежу, в диапазон которого попадает объект Number.
    """
    def __init__(
        self, 
        mappable: dict[tuple[Number, Number], Any]
    ):
        try:
            for key1, key2 in mappable:
                if isinstance(key1, Number) and isinstance(key2, Number):
                    if key1 < key2:
                        continue
                    else:
                        raise ValueError('key1 must be lower than key2')
                else:
                    raise TypeError('key1 and key2 both must be numbers')
        
        except ValueError:
            raise ValueError('range must be set by two numbers')
        
        except TypeError:
            raise TypeError('keys must be tuples with two numbers')
        
        else:
            # self.update(mappable)
            self |= mappable
    
    def __getitem__(self, key: Number):
        if isinstance(key, Number):
            for keys, value in self.items():
                left, right = keys
                if left <= key <= right:
                    return value
        else:
            # нарушение LSP — невозможность обращения по истинному ключу
            # raise TypeError
            
            # решение — предоставить возможность обратиться по истинному ключу
            return super().__getitem__(key)


health = DictOfRanges({
    (0, 15): 'при смерти',
    (16, 40): 'тяжело ранен',
    (41, 85): 'ранен',
    (86, 100): 'здоров',
})

# нарушение LSP — невозможность обращения по истинному ключу
# >>> health[(0, 15)]
# ...
# TypeError: '<=' not supported between instances of 'int' and 'tuple'

# решение
# >>> health[(86, 100)]
# 'здоров'
