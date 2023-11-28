"""Демонстратор простой фабрики."""

class Person:
    def __init__(self, id_: int, name: str):
        self.id = id_
        self.name = name
    
    def __str__(self):
        return f"{self.name} ({self.id})"


class PersonFactory:
    """Создаёт и нумерует экземпляры Person используя атрибут экземпляра."""
    def __init__(self):
        self.id = 0
    
    def create_person(self, name: str) -> Person:
        self.id += 1
        return Person(self.id, name)


class PersonFactoryCommon:
    """Создаёт и нумерует экземпляры Person используя поле класса."""
    id_ = 0
    
    @classmethod
    def create_person(cls, name: str) -> Person:
        cls.id_ += 1
        return Person(cls.id_, name)


pf = PersonFactory()
p1 = pf.create_person('Ярослав')
p2 = pf.create_person('Святослав')
p3 = pf.create_person('Владислав')
print(p1, p2, p3, sep='\n', end='\n\n')

# Ярослав (1)
# Святослав (2)
# Владислав (3)

p4 = PersonFactoryCommon.create_person('Анна')
p5 = PersonFactoryCommon.create_person('Елизавета')
p6 = PersonFactoryCommon.create_person('Алиса')
print(p4, p5, p6, sep='\n', end='\n\n')

# Анна (1)
# Елизавета (2)
# Алиса (3)

pf2 = PersonFactory()
p7 = pf2.create_person('John')
p8 = pf2.create_person('Max')
print(p7, p8, sep='\n', end='\n\n')

# John (1)
# Max (2)

p9 = pf.create_person('Вячеслав')
print(p9, end='\n\n')

# Вячеслав (4)

del p8
p10 = pf2.create_person('Alan')
print(p10)

# Alan (3)
