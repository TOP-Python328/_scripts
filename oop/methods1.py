from pathlib import Path
from sys import path


DIR = Path(path[0])


# для имён классов используется ВерблюжийРегистр (CamelCase)
class JournalFileInterface:
    default_path: Path = DIR / 'journal.log'
    
    @classmethod
    def append(cls, journal_entry: str, journal_path: str | Path = None) -> Path:
        if journal_path:
            journal_path = Path(journal_path)
            if not journal_path.is_absolute():
                journal_path = DIR / journal_path
        else:
            journal_path = cls.default_path
        
        with open(journal_path, 'a', encoding='utf-8') as journal_file:
            print(journal_entry, file=journal_file)
        
        return journal_path


# >>> JournalFileInterface.append
# <bound method JournalFileInterface.append of <class '__main__.JournalFileInterface'>>

# >>> JournalFileInterface.append('def')
# WindowsPath('D:/G-Doc/TOP Academy/Python web/328/scripts/oop/journal.log')

# при вызове классового метода от класса происходит подмена вызова:
# JournalFileInterface.append(*args) --> JournalFileInterface.append(JournalFileInterface, *args)


# >>> jfi = JournalFileInterface()

# >>> jfi.append
# <bound method JournalFileInterface.append of <class '__main__.JournalFileInterface'>>

# >>> jfi.append('zxc')
# WindowsPath('D:/G-Doc/TOP Academy/Python web/328/scripts/oop/journal.log')

# при вызове классового метода от экземпляра происходит подмена вызова:
# jfi.append(*args) --> jfi.__class__.append(jfi.__class__, *args)

