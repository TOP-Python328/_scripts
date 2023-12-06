"""
Model (MVC): получение данных.
"""

from dataclasses import dataclass
from json import load as jload
from pathlib import Path
from pprint import pprint
from sys import path


people_path = Path(path[0]) / 'people.json'


@dataclass
class Person:
    name: str
    age: int
    email: str
    phone: str
    langs: set[str]
    country: str
    
    def __repr__(self):
        return f'{self.name} from {self.country} speaks {" ".join(self.langs)}'


def read_all_people(data_path: str | Path = None) -> list[Person]:
    if data_path is None:
        data_path = people_path
    with open(data_path, encoding='utf-8') as filein:
        raw_data = jload(filein)
    result = []
    for obj in raw_data:
        obj['langs'] = set(obj['langs'].split())
        result.append(Person(**obj))
    return result


storage: list[Person] = []
all_langs = {'RU', 'SP', 'CH', 'FR', 'DE', 'JP', 'KZ', 'EN', 'IT'}


if __name__ == '__main__':
    
    storage = read_all_people()
    pprint(storage, sort_dicts=False)

    # >>> type(storage[0])
    # <class '__main__.Person'>
    
    # >>> storage[0].__dict__
    # {'name': 'Isaac Jimenez', 'age': 58, 'email': 'isaacjimenez7572@mail.edu', 'phone': '+7-918-323-4712', 'langs': {'JP', 'SP', 'IT'}, 'country': 'Kazakhstan'}

