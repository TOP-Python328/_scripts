"""
View (MVC): представление с интерфейсом командной строки.
"""

from collections.abc import Iterable


def greeting() -> None:
    print('Приветствую в демонстраторе MVC!')


def get_command() -> str:
    return input('\n введите команду > ')


def wrong_lang(allowed_langs: Iterable[str]) -> None:
    print(f' используйте языки: {" ".join(allowed_langs)}')


def people(data: Iterable[str]) -> None:
    print(*data, sep='\n')


def bye() -> None:
    print('\nПока!')

