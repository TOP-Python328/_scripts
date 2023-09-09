from json import loads, dumps, dump
from pathlib import Path
from pprint import pprint
from sys import path


data = Path(path[0]) / 'stdlib10.json'
data = data.read_text(encoding='utf-8')
data = loads(data)

pprint(data, sort_dicts=False)
# [{'_id': '_b_mountains',
#   'name': 'Горы',
#   'changed': False,
#   'enter condition': {},
#   'zones': ['_z_plateau', '_z_scarp', '_z_rocks', '_z_nek']},
#  {'_id': '_z_plateau',
#   'name': 'Плато',
#   'points': ['_p_plain',
#              '_p_small_boulders',
#              '_p_small_boulders_herbivorous_attack',
#              '_p_large_boulders',
#              '_p_large_boulders_predator_attack']},
#  {'_id': '_z_scarp', 'name': 'Крутой склон', 'points': []},
#  {'_id': '_z_rocks', 'name': 'Скалы', 'points': []}]

data[2]['points'].extend(('_p_rocks', '_p_rocks_predator_attacks'))
print(dumps(data))
# [{"_id": "_b_mountains", "name": "\u0413\u043e\u0440\u044b", "changed": false, "enter condition": {}, "zones": ["_z_plateau", "_z_scarp", "_z_rocks", "_z_nek"]}, {"_id": "_z_plateau", "name": "\u041f\u043b\u0430\u0442\u043e", "points": ["_p_plain", "_p_small_boulders", "_p_small_boulders_herbivorous_attack", "_p_large_boulders", "_p_large_boulders_predator_attack"]}, {"_id": "_z_scarp", "name": "\u041a\u0440\u0443\u0442\u043e\u0439 \u0441\u043a\u043b\u043e\u043d", "points": ["_p_rocks", "_p_rocks_predator_attacks"]}, {"_id": "_z_rocks", "name": "\u0421\u043a\u0430\u043b\u044b", "points": []}]

data_path = Path(path[0]) / 'stdlib10_edited.json'
with open(data_path, 'w', encoding='utf-8') as fileout:
    dump(data, fileout, ensure_ascii=False, indent=2)
