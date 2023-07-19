while True:
    command = input(' > ')
    if command == 'quit':
        break
    elif command == 'line':
        print('—'*60)

print('первый цикл завершён')


command = input(' > ')
while command != 'quit':
    if command == 'line':
        print('—'*60)
    command = input(' > ')

print('второй цикл завершён')

