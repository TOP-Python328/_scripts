fruits = [
    'яблоко',
    'банан',
    'персик',
    'арбуз',
    'слива',
]

for i in range(len(fruits)):
    fruits[i] = fruits[i].upper()
print(fruits)


for i, fruit in enumerate(fruits):
    fruits[i] = fruit.capitalize()
print(fruits)


# >>> for elem in enumerate('word1 word2'):
# ...     print(elem)
# ...
# (0, 'w')
# (1, 'o')
# (2, 'r')
# (3, 'd')
# (4, '1')
# (5, ' ')
# (6, 'w')
# (7, 'o')
# (8, 'r')
# (9, 'd')
# (10, '2')

# распаковка:
# >>> t = (1, 2)
# >>> n, m = t
# >>> n
# 1
# >>> m
# 2

