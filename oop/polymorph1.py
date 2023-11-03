elements1 = [1, 2, '3', '4', 5.6]
elements2 = [7, '8', '9', 10, 11+1j]


for item1, item2 in zip(elements1, elements2):
    try:
        print(item1 + item2)
    except TypeError as exc:
        print(exc)

