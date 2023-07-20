try:
    ...
except:
    ...
else:
    ...
finally:
    ...


a = 12
try:
    print(a + int(input(' число: ')) / 0)
except NameError:
    print('перехват NameError')
except ZeroDivisionError:
    print('перехват ZeroDivisionError')


print('программа завершена корректно')
