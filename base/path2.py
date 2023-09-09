from pathlib import Path
from sys import path


datafile_path = Path(path[0]) / '_questionnaire.py'


# машиночитаемое строковое представление выводится в stdout
# >>> datafile_path
# WindowsPath('D:/G-Doc/TOP Academy/Python web/328/scripts/base/_questionnaire.py')

# человекочитаемое строковое представление выводится в stdout
# >>> print(datafile_path)
# D:\G-Doc\TOP Academy\Python web\328\scripts\base\_questionnaire.py


# >>> datafile_path.name
# '_questionnaire.py'
# >>>
# >>> datafile_path.stem
# '_questionnaire'
# >>>
# >>> datafile_path.suffix
# '.py'


# >>> datafile_path.parent
# WindowsPath('D:/G-Doc/TOP Academy/Python web/328/scripts/base')
# >>>
# >>> datafile_path.parent.name
# 'base'
# >>>
# >>> datafile_path.parent.suffix
# ''
# >>>
# >>> datafile_path.parents
# <WindowsPath.parents>
# >>>
# >>> for p in datafile_path.parents:
# ...     print(p)
# ...
# D:\G-Doc\TOP Academy\Python web\328\scripts\base
# D:\G-Doc\TOP Academy\Python web\328\scripts
# D:\G-Doc\TOP Academy\Python web\328
# D:\G-Doc\TOP Academy\Python web
# D:\G-Doc\TOP Academy
# D:\G-Doc
# D:\


# >>> datafile_path = datafile_path.parent / 'data'
# >>> datafile_path
# WindowsPath('D:/G-Doc/TOP Academy/Python web/328/scripts/base/data')
# >>>
# >>> datafile_path.exists()
# True
# >>>
# >>> datafile_path.is_dir()
# False
# >>>
# >>> datafile_path.is_file()
# True


# только для nt систем
# >>> datafile_path.drive
# 'D:'

# только для posix систем
# >>> datafile_path.root
# '\\'

# универсально
# >>> datafile_path.anchor
# 'D:\\'


# >>> Path.cwd()
# WindowsPath('D:/G-Doc/TOP Academy/Python web/328')
# >>>
# >>> Path.home()
# WindowsPath('G:/Users/Геннадий')

