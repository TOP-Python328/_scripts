# старшая карта
# (2, 4, 10, 14, 5)
# пара
# (5, 7, 10, 4, 5)
# две пары
# (4, 5, 6, 8, 5)
# сет
# (7, 7, 2, 14, 7)
# стрит
# (4, 5, 6, 7, 8)
# фулл-хаус
# (4, 5, 4, 4, 5)
# каре
# (5, 5, 5, 4, 5)

while True:
    inp = input('\n > ')
    if not inp:
        break
    hand = [int(card) for card in inp.split()]
    # unique --> {4, 10}
    result = 'старшая карта'

    unique = set(hand)
    unique_len = len(unique)
    max_rate = max(hand.count(card) for card in hand)

    if unique_len == 4:
        result = 'пара'

    elif unique_len == 3:
        if max_rate == 2:
            result = 'две пары'
        else:
            result = 'сет'

    elif unique_len == 5:
        hand_sort = sorted(hand)
        if hand_sort == list(range(hand_sort[0], hand_sort[0]+5)):
            result = 'стрит'

    elif unique_len == 2:
        if max_rate == 3:
            result = 'фулл-хаус'
        else:
            result = 'каре'

    print(result)
