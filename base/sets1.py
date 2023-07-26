salaries = {45000.0, 55000.0, 40000.0, 45000.0}

print(type(salaries))
print(salaries)

print(f'\n{len(salaries) = }\n')

for salary in salaries:
    print(salary)
print()


days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
days_unique = set(days.values())

print(days_unique)


# >>> empty_dict = {}
# >>> type(empty_dict)
# <class 'dict'>

# >>> empty_set = set()
# >>> type(empty_set)
# <class 'set'>
