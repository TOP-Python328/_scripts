# примеры преобразования в объект int

# bool
print(int(True))
print(int(False))

# float
print(int(9.1))
print(int(-10.89))

# str
print(int('24'))
print(int('-5'))
# приведёт к ValueError
# print(int('5-'))
# print(int('10 20'))
# print(int('9.3'))
# print(int('ff'))

print(int('ff', base=16))
print(int('11111111', base=2))
