# импорт внешних пакетов
from sqlalchemy import create_engine, text
# импорт из стандартной библиотеки
from json import load as jload
from pathlib import Path
from re import fullmatch
from sys import path


# шаблон строки для подключения к БД:
# dialect[+driver]://user:password@host[:port]/dbname[?key=value..]

# пример того, как может выглядеть строка для подключения к конкретной БД
# mysql_url = 'mysql+mysqlconnector://root:root@127.0.0.1:3300/world'

# чтение конфиденциальных данных
dbconfig_path = Path(path[0]) / 'db.config'
with open(dbconfig_path, encoding='utf-8') as filein:
    dbconfig: dict = jload(filein)

# формирование строки подключения для создания объекта движка
dialect = 'mysql'
mysql_url = (
    f"{dialect}"
    f"+{dbconfig[dialect]['dbapi']}"
    f"://{dbconfig[dialect]['user']}"
    f":{dbconfig[dialect]['password']}"
    f"@{dbconfig[dialect]['host']}"
    f":{dbconfig[dialect]['port']}"
    + (f"/{dbname}" if (dbname := dbconfig[dialect].get('database', '')) else '')
)

# создание объекта движка
engine = create_engine(mysql_url)

# изучение публичных атрибутов объекта движка
# for attr in dir(engine):
#     if not fullmatch(r'_{1,2}\w+(_{2})?', attr):
#         value = getattr(engine, attr)
#         print(f"{attr}\n\t{type(value)}\n\t{value}\n")

# предобработка текста SQL запросов
select_world_capitals = text(
    "select country.name as 'Country',\n"
    "	    city.name as 'Capital'\n"
    "  from country\n"
    "  join city\n"
    "    on country.capital = city.id;\n"
)

# работа с объектом подключения
with engine.connect() as conn:
    # метод execute() возвращает курсор
    cursor = conn.execute(select_world_capitals)
    # извлекаем данные из курсора
    capitals = cursor.fetchall()

for row in capitals:
    print(row)
print('\n\n')

