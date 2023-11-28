"""Демонстратор одиночки."""

from typing import Self


class Singleton:
    __instance: Self = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
            return cls.__instance
        else:
            return cls.__instance


# >>> st1 = Singleton()
# вместо создания нового экземпляра будет возвращён ранее созданный
# >>> st2 = Singleton()
# >>>
# >>> print(f'{st1 is st2 = }')
# st1 is st2 = True

# уязвимость
# >>> Singleton._Singleton__instance = None
# >>> st3 = Singleton()
# >>>
# >>> print(f'{st3 is st1 = }')
# st3 is st1 = False
