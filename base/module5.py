from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
from sys import path, modules


file_path = Path(path[0]) / '1.py'
name = 'модуль 1.py'

# создание объекта спецификации
spec = spec_from_file_location(name, file_path)
# создание объекта модуля и его ассоциирование с индентификатором в глобальном пространстве имён
module5 = module_from_spec(spec)
# добавление ссылки на объект модуля в словарь всех 
modules[name] = module5
# выполнение кода модуля
spec.loader.exec_module(module5)

# импорт модуля завершён
# >>>
# >>> module5
# <module 'модуль 1.py' from 'D:\\G-Doc\\TOP Academy\\Python web\\328\\scripts\\base\\1.py'>
# >>>
# >>> module5.data
# {'a': 152}
