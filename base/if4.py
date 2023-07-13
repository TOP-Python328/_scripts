# >>> 'A' if 1 == 1 else 'B'
# 'A'
# >>> 'A' if 1 == 2 else 'B'
# 'B'
# >>> 'A'*5 if 1 == 1 else 'B'*5
# 'AAAAA'
# >>> 'A'*5 if 1 == 3 else 'B'*5
# 'BBBBB'


DEBUG = False

text = input(' введите текст: ')

debug_data = f'{len(text)}\n' if DEBUG else ''

print(f'{debug_data}{text}')
