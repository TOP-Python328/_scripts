text = input(' фраза: ')
cnt = 0

for char in text:
    if char == ' ':
        cnt += 1

print(f'в строке {cnt+1} слова')
