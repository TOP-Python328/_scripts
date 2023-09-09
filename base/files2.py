from pathlib import Path
from sys import path


datafile_path = Path(path[0]) / 'data'

# filein — файлоподобный объект
filein = open(datafile_path, encoding='utf-8')

text = filein.read()
# line и lines будут пустыми, так как файлоподобные объекты работают по принципу генераторов
# line = filein.readline()
# lines = filein.readlines()

filein.close()


filein = open(datafile_path, encoding='utf-8')

lines = []
for line in filein:
    lines.append(line.strip())

filein.close()

