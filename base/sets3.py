cyrillic = {chr(char_code) for char_code in range(1040, 1104)} | {'ё', 'Ё'}

print(f'{len(cyrillic) = }\n')

print(f"{'ё' in cyrillic = }")
print(f"{' ' in cyrillic = }")
print(f"{'!' not in cyrillic = }")
