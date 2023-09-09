from pathlib import Path
from sys import path


datafile_path = Path(path[0]) / 'data'


with open(datafile_path, encoding='utf-8') as filein:
    text = filein.read()


with open(datafile_path, 'a', encoding='utf-8') as fileout:
    # fileout.write(text)
    print(*text.split('\n'), sep='!', file=fileout)

