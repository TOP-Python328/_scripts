cnt = 10
while cnt > 0:
    cnt -= 1
else:
    print('цикл завершён корректно')
# print(f'cnt = {cnt}')
print(f'{cnt=}')


cnt = 10
while cnt > 0:
    cnt -= 1
    # if cnt % 7 == 0:
    if not cnt % 7:
        break
else:
    print('цикл завершён корректно')
print(f'{cnt=}')

