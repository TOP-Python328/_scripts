from pathlib import Path
from pprint import pprint
from sqlite3 import connect, Row
from sys import path


script = '''
create table if not exists test (
  id int primary key,
  column varchar(100) not null
);
'''


db_path = Path(path[0]) / 'db.sqlite3'

# создание и настройка объекта подключения
connection = connect(db_path)
# для Python 3.12:
# connection.autocommit = True

# создание объекта курсора
cursor = connection.cursor()

# "размещение" запросов в объект курсора (упаковка запросов в транзакцию) и отправка запроса SQL-движку
cursor.executescript(script)

# подтверждение транзакции
connection.commit()

# запросы выборки в подтверждении не нуждаются
cursor.execute('select * from books')

# >>> pprint(cursor.fetchall())
# [(1, 'Осколки чести', 1),
#  (2, 'Барраяр', 1),
#  (3, 'Спектр', 2),
#  (4, 'Осенние визиты', 2),
#  (5, 'Вино из одуванчиков', 3),
#  (6, 'Электрическое тело, пою', 3)]

# >>> cursor.fetchall()
# []

# использование словароподобных объектов Row для извлечения данных из курсора
cursor.row_factory = Row

cursor.execute('select * from authors')

# без разницы как извлекать данные из курсора
data = []
for row in cursor:
    data.append(row)

# >>> pprint(data)
# [<sqlite3.Row object at 0x0000028828BD1330>,
#  <sqlite3.Row object at 0x0000028828BD1630>,
#  <sqlite3.Row object at 0x0000028828BD16C0>]

# >>> data[0].keys()
# ['id', 'first_name', 'last_name']
# >>>
# >>> data[0]['first_name']
# 'Лоис'

# >>> cursor.fetchall()
# []


cursor.row_factory = None

cursor.execute('''
select last_name,
       title
  from books as b
  join autors as a
    on a.id = b.author_id
''')
pprint(cursor.fetchall())

# [('Буджолд', 'Осколки чести'),
#  ('Буджолд', 'Барраяр'),
#  ('Лукьяненко', 'Спектр'),
#  ('Лукьяненко', 'Осенние визиты'),
#  ('Брэдбери', 'Вино из одуванчиков'),
#  ('Брэдбери', 'Электрическое тело, пою')]

