from pathlib import Path
from re import compile
from sys import path


scripts_dir = Path(path[0]).parent

for path_ in scripts_dir.iterdir():
    if path_.is_dir():
        print(path_)
print()

for path_ in scripts_dir.glob('*.txt'):
    print(path_)
print()

pat_filename = compile(r'\w*\d{1,2}\.py')
for path_ in (scripts_dir / 'base').iterdir():
    if pat_filename.fullmatch(path_.name):
        print(path_.name)
print()
