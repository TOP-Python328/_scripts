table = [(14, 'там'), (9, 'и'), (5, 'на'), (2, 'я'), (2, 'через'), (2, 'учёный'), (2, 'у'), (2, 'с'), (2, 'моря'), (2, 'кот'), (2, 'идёт'), (2, 'зелёный'), (2, 'дуб'), (2, 'в'), (2, 'без'), (1, 'ясных'), (1, 'ягой'), (1, 'чудеса'), (1, 'чредой'), (1, 'чахнет'), (1, 'цепь'), (1, 'цепи'), (1, 'царя'), (1, 'царь'), (1, 'царевна'), (1, 'ходит'), (1, 'тужит'), (1, 'тридцать'), (101, 'том'), (1, 'темнице'), (1, 'ступа'), (1, 'стоит'), (1, 'собой'), (1, 'служит'), (1, 'следы'), (1, 'сказку'), (1, 'сказки'), (1, 'сидит'), (1, 'сидел'), (1, 'свои'), (1, 'сама'), (1, 'русью'), (1, 'русский'), (1, 'русалка'), (1, 'пустой'), (1, 'прихлынут'), (1, 'прекрасных'), (1, 'полны'), (22, 'под'), (1, 'по'), (1, 'пленяет'), (1, 'пил'), (1, 'песчаный'), (1, 'песнь'), (1, 'перед'), (1, 'пахнет')]


# word_width = max(len(word) for rate, word in table)
# rate_width = max(len(str(rate)) for rate, word in table)

widths = [
    max(len(str(obj)) for obj in column)
    for column in zip(*table)
]

table_str = '\n'.join(
    # f'| {word.ljust(word_width)} | {str(rate).center(rate_width)} |'
    f'| {word:<{widths[1]}} | {rate:^{widths[0]}} |'
    for rate, word in table
)

print(table_str)
