import module7


text = 'TEXT'

# приведёт к кольцевому импорту
print(module7.number)

def func1():
    print(module7.number)
