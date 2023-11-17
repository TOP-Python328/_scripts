"""Single Responsibility Principle — Принцип Единственной Ответственности"""

from datetime import datetime as dt
from pathlib import Path
from sys import path


class Journal:
    """
    Ведение журнала, работа с записями.
    """
    default_format: str = '%Y-%m-%d %H:%M:%S'
    # нарушение SRP
    # default_path: Path = Path(path[0]) / 'solid_srp.log'
    
    def __init__(self):
        self.entries: list[str] = []
    
    def __str__(self):
        return '\n'.join(self.entries)
    
    def add_entry(self, new_entry: str) -> None:
        self.entries.append(f'{dt.now():{self.default_format}} — {new_entry}')
    
    # нарушение SRP
    # def save_file(self, path: Path = None) -> None:
    #     if path is None:
    #         path = self.default_path
    #     path.write_text(str(self), encoding='utf-8')


# для соблюдения SRP выводим в отдельный класс функциональность по сохранению в файл
class FileIO:
    """
    Работа с путями, взаимодействие с файловой системой.
    """
    default_path: Path = Path(path[0]) / 'solid_srp.log'
    
    @classmethod
    def save_to_file(cls, data: str, path: Path = None) -> None:
        if path is None:
            path = cls.default_path
        path.write_text(data, encoding='utf-8')

