fruits = ('pear', 'melon', 'peach', 'citron', 'lime', 'apple')
colors = ('mud-green', 'yellow', 'orange-red', 'light-yellow', 'green')

colored_fruits_list = '\n'.join(
    f'{colors[i]} {fruits[i]}'
    for i in range(min(len(fruits), len(colors)))
)
print(colored_fruits_list, end='\n\n')

colored_fruits_list = '\n'.join(
    f'{color} {fruit}'
    for color, fruit in zip(colors, fruits)
)
print(colored_fruits_list, end='\n\n')

