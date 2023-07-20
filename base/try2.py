while True:
    num = input(' число > ')
    if not num:
        break
    elif num.isdecimal():
        num = int(num)
    else:
        print(' ! вводите только цифры')
print('конец первого цикла\n')


while True:
    try:
        num = input(' число > ')
        num = int(num)
    except ValueError:
        if not num:
            break
        print(' ! вводите только цифры')
print('конец второго цикла\n')

