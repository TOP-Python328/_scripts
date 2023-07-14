a = [1, 2, 3]
# в переменную b записывается ссылка на изменяемый объект, связанный с переменной a
b = a

print(
    id(a),
    id(b),
    sep='\n',
    end='\n\n'
)

a[0] = 1000

print(a)
print(b, end='\n\n')

c = a.copy()

print(
    id(a),
    id(c),
    sep='\n',
    end='\n\n'
)

c[2] = 3000

print(a)
print(c, end='\n\n')
