"""
Dependencies Inversion Principle — Принцип Инверсии Зависимостей

Средний уровень
"""

import solid_dip_low as model


db = model.Relationship()

__ivan = model.Person('Иван')
__anna = model.Person('Анна')
__liza = model.Person('Елизавета')
__petr = model.Person('Пётр')
__igor = model.Person('Игорь')
__alla = model.Person('Алла')

db.add_relation(__ivan, __liza)
db.add_relation(__ivan, __petr)
db.add_relation(__anna, __liza)
db.add_relation(__anna, __petr)
db.add_relation(__igor, __alla)

