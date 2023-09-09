from pathlib import Path
from string import digits, whitespace
from sys import path


datafile_path = Path(path[0]) / 'data'

text = datafile_path.read_text(encoding='utf-8')

# >>> text
# 'line 1\nстрочка 2\n'
# >>>
# >>> print(text.split('\n'))
# ['line 1', 'строчка 2', '']

text = '\n'.join(
    line.strip(digits + whitespace) 
    for line in text.strip().split('\n')
)

# >>> digits
# '0123456789'
# >>>
# >>> whitespace
# ' \t\n\r\x0b\x0c'
# >>>
# >>> text
# 'line\nстрочка'

datafile_path.write_text(text, encoding='utf-8')


# >>> datafile_path.parent.read_text(encoding='utf-8')
# ...
# PermissionError: [Errno 13] Permission denied: 'D:\\G-Doc\\TOP Academy\\Python web\\328\\scripts\\base'

# >>> (datafile_path.parent / 'config.ini').read_text(encoding='utf-8')
# ...
# FileNotFoundError: [Errno 2] No such file or directory: 'D:\\G-Doc\\TOP Academy\\Python web\\328\\scripts\\base\\config.ini'


