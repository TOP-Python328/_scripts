# создание объекта с помощью литерала
num1 = 5
# создание объекта с помощью конструктора класса
num1_ = int(5)

num2 = True
num2_ = bool(0)

num3 = 3.01
num3_ = float(4)

num4 = 1+1j
num4_ = complex(1, -5)

num5 = 'PYTHON'
num5_ = str('литерал')

num6 = b'00FF12AE'
num6_ = bytes('PYTHON', encoding='utf-8')

num7 = (6,)
num7_ = tuple((1, 9, 2))

num8 = [4.1]
num8_ = list((0.01, 0.02, 0.03))

num9 = {'a': 1, 'b': 2}
num9_ = dict([(0.9, 100), ('ten', 10), [10, 'десять'], 'ab'])

num10 = {1, 7, 'z'}
num10_ = set('abba')

# для неизменяемого множества и всех прочих типов литералы отсутствуют
num11 = frozenset([2, 3, 4])
