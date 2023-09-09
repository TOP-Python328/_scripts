from pathlib import Path
from pprint import pprint
from sys import path
from tomllib import loads


config = Path(path[0]) / 'stdlib8.toml'
config = config.read_text(encoding='utf-8')
config = loads(config)

# >>> pprint(config, sort_dicts=False)
# {'build-system': {'requires': ['multimethod>=1.1']},
#  'tool': {'pytest': {'ini_options': {'pythonpath': 'sources',
#                                      'addopts': ['--import-mode=importlib']}}}}

