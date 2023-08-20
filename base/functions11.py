def func(**kwargs):
    print(f'\n{type(kwargs)}\n{kwargs}')


func()
func(a=1, b=2)
func(**{'x': -4, 'y': 0, 'z': 11})
