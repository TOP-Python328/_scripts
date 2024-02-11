# импорт внешних пакетов
from mysql.connector import connect
# импорт из стандартной библиотеки
from json import loads as jloads
from pathlib import Path
from pprint import pprint
from sys import path


config_path = Path(path[0]) / 'db.config'
config = jloads(config_path.read_text(encoding='utf-8'))

script = '''
select *
  from departments as dep
  join donations as don
    on dep.id = don.departments_id
   and dep.id = 3
'''

with connect(**config) as con:
    with con.cursor() as cur:
        cur.execute(script)
        pprint(cur.fetchall(), width=100)

# [(3, 'Кардиологическое отделение', 15, Decimal('1450246.00'), datetime.date(2014, 12, 15), 3, 10),
#  (3, 'Кардиологическое отделение', 33, Decimal('780396.00'), datetime.date(2001, 4, 26), 3, 6),
#  (3, 'Кардиологическое отделение', 38, Decimal('480300.00'), datetime.date(2019, 12, 11), 3, 11),
#  (3, 'Кардиологическое отделение', 39, Decimal('206213.00'), datetime.date(2006, 11, 7), 3, 12),
#  (3, 'Кардиологическое отделение', 45, Decimal('772941.00'), datetime.date(2002, 10, 29), 3, 12),
#  (3, 'Кардиологическое отделение', 61, Decimal('682265.00'), datetime.date(2009, 4, 7), 3, 2),
#  (3, 'Кардиологическое отделение', 69, Decimal('957355.00'), datetime.date(2006, 12, 22), 3, 10)]

