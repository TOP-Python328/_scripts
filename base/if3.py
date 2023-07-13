n = int(input('\n число: '))

if 0 <= n and n < 10:
    print('один разряд')

elif 10 <= n and n < 100:
    print('два разряда')

elif 100 <= n < 1000:
    print('три разряда')


angle = float(input('\n угол в радианах: '))

if angle < 3.1415/2 or 3*3.1415/2 < angle:
    print('первая и третья тригонометрические четверти')


word = input('\n слово: ')

if not word:
    print('... пусто')
