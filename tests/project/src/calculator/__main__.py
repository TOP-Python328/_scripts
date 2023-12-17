print('точка входа', end='\n\n')

print(__package__, end='\n\n')

# имя корневого пакета доступно, если корневой пакет импортирован
from calculator import app
# относительный импорт из текущего пакета
from . import io

print(app, end='\n\n')

print(app.model, end='\n\n')

print(app.model.utils, end='\n\n')

