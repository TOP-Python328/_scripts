numbers = [20, 14, 53, 33, 28]
average = sum(numbers) / len(numbers)

generator = (n/average for n in numbers)

print(type(generator))
print(generator, end='\n\n')

# >>> print(*numbers)
# 20 14 53 33 28

# >>> print(numbers[0], numbers[1], numbers[2], numbers[3], numbers[4])
# 20 14 53 33 28

for n in generator:
    print(n)

# не выведет ничего, потому что проитерироваться по генератору возможно только один раз
print(*generator, end='\n\n')
