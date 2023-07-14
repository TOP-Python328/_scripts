numbers = [1, 2, 3.3, '4', [5, 6.6]]

print(
    numbers,
    type(numbers),
    id(numbers),
    sep='\n',
    end='\n\n'
)

print(
    numbers[2],
    numbers[-1],
    sep='\n',
    end='\n\n'
)

print(numbers[-1][0], end='\n\n')


numbers[0] = 100
print(id(numbers))

numbers.append(7)
print(id(numbers))

numbers += [8.8]
print(id(numbers))

numbers = numbers + [9]
print(id(numbers), end='\n\n')

print(numbers)
