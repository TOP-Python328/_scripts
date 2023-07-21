numbers = [20, 14, 53, 33, 28]
average = sum(numbers) / len(numbers)

# numbers_normalized = []
# for n in numbers:
    # numbers_normalized += [n/average]

numbers_normalized = list(n/average for n in numbers)
print(numbers_normalized)

numbers_normalized = [n/average for n in numbers]
print(numbers_normalized)

print(min(n/average for n in numbers))
