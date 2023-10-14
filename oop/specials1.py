class Test:
    def __del__(self):
        print('вызов __del__()')


var = Test()
numbers = [var, var]

print('первая операция')
var = 'abc'
print('вторая операция')
numbers[0] = 'xyz'

