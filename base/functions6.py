flag = False
for num1 in range(2, 6):
    for num2 in range(4, 7):
        if num1 * num2 > 15:
            flag = True
            break
    if flag:
        break
print(f'минимальные числа, произведение которых больше 15: {num1} и {num2}')



def find_multipliers(product: int) -> tuple[int, int]:
    for num1 in range(2, 6):
        for num2 in range(4, 7):
            if num1 * num2 > 15:
                return num1, num2


num1, num2 = find_multipliers(15)
print(f'минимальные числа, произведение которых больше 15: {num1} и {num2}')
