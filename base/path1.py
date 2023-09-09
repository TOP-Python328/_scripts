# абсолютные пути
# posix
'/home/genndalf/docs/text.txt'
# nt
r'c:\users\genndalf\docs\text.txt'
'c:\\users\\genndalf\\docs\\text.txt'

# относительные пути
# posix: /home/genndalf
'docs/text.txt'
# nt: c:\users\genndalf
r'docs\text.txt'
'docs\\text.txt'


from os import name
from sys import path


if name == 'nt':
    PATH_SPLITTER = '\\'
else:
    PATH_SPLITTER = '/'


datafile_name = '_questionnaire.py'
datafile_path = PATH_SPLITTER.join((path[0], datafile_name))

print(datafile_path)
