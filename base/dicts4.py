products = {
    'фрукты': ['яблоко', 'персик', 'слива'],
    'крупы': ['гречка', 'рис', 'манка'],
    'молочные': ['молоко', 'сметана', 'сливки'],
}
# products = {
    # 'фрукты': 12,
    # 'крупы': 34,
    # 'молочные': 56,
# }


for key in products:
    # print(key, end=' ')
    # print(products[key])
    products[key].pop()

# >>> products
# {'фрукты': ['яблоко', 'персик'], 'крупы': ['гречка', 'рис'], 'молочные': ['молоко', 'сметана']}

for value in products.values():
    # print(value)
    value.append('')
    # value = 5

# >>> products
# {'фрукты': ['яблоко', 'персик', ''], 'крупы': ['гречка', 'рис', ''], 'молочные': ['молоко', 'сметана', '']}

for key, value in products.items():
    # print(key, value)
    if '' in value:
        value.remove('')
    products[key] = value[::-1]

# >>> products
# {'фрукты': ['персик', 'яблоко'], 'крупы': ['рис', 'гречка'], 'молочные': ['сметана', 'молоко']}
