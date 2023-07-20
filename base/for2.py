fruits = [
    'яблоко',
    'банан',
    'персик',
    'арбуз',
    'слива',
]
indexes = (0, 1, 2, 3, 4)


for fruit in fruits:
    if fruit == 'арбуз':
        print('арбуз — это ягода!')
        fruit = 'груша'
print(fruits, end='\n\n')


for i in indexes:
    if fruits[i] == 'арбуз':
        print('арбуз — это ягода!')
        fruits[i] = 'груша'
print(fruits, end='\n\n')

