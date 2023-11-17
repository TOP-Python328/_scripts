"""
Dependencies Inversion Principle — Принцип Инверсии Зависимостей

Верхний уровень
"""

import solid_dip_med as storage


class Research:
    def __init__(self, database: storage.model.Relationship):
        self.db = database
    
    def find_all_children(
            self, 
            person: storage.model.Person
    ) -> list[storage.model.Person]:
        # нарушение DIP — сформирована зависимость от конкретной реализации кода нижнего уровня
        # for person1, relation, person2 in self.db.storage:
        #     if person == person1:
        #         if relation is storage.model.Relation.PARENT:
        #             yield person2
        
        # решение — использовать предоставленный интерфейс
        return list(self.db.find_all_children(person))


r = Research(storage.db)

