import module6


number = 159

print(dir(module6))

# приведёт к кольцевому импорту
print(module6.text)

def func2():
    print(module6.text)
