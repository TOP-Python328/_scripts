from random import choice, randrange as rr
from typing import Self


class Cat:
    names = ('Беляш', 'Черныш', 'Мурка', 'Рыж', 'Кыс', 'Барсик')
    colors = ('белый', 'чёрный', 'полосатый', 'черепаховый', 'рыжий')
    
    def __init__(self, name: str = None, color: str = None):
        if not name:
            name = choice(self.names)
        self.name = name
        if not color:
            color = choice(self.colors)
        self.color = color
    
    def __repr__(self):
        return f'<{self.name}: {self.color}>'
    
    def __str__(self):
        return self.name
    
    @staticmethod
    def meow() -> str:
        """"""
        return 'мяу'
    
    def hungry(self) -> str:
        """"""
        return '-'.join(self.meow() for _ in range(rr(2, 5)))
    
    @classmethod
    def reproduce(cls) -> list[Self]:
        """"""
        return [cls() for _ in range(rr(2, 5))]


if __name__ == '__main__':
    yara = Cat('Яра', 'серо-полосатая')

# >>> yara
# <Яра: серо-полосатая>
# >>>
# >>> yara.meow()
# 'мяу'
# >>>
# >>> yara.hungry()
# 'мяу-мяу-мяу-мяу'
# >>>
# >>> yara.hungry()
# 'мяу-мяу'
# >>>
# >>> yara.hungry()
# 'мяу-мяу-мяу'
# >>>
# >>> kittens = yara.reproduce()
# >>>
# >>> for kitty in kittens:
# ...     print(f'{kitty.name}, {kitty.color}')
# ...
# Рыж, чёрный
# Мурка, рыжий
# Барсик, черепаховый
# >>>
# >>> print(*kittens)
# Рыж Мурка Барсик
