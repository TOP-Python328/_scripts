a = 10
d = {'key': 'value'}


def test(param=None):
    global a
    
    b = 20
    print(
        'глобальное пространство имён: взгляд из функции', 
        *(f'{k}: {v!r}' for k, v in globals().items() if not k.endswith('__')), 
        sep='\n', end='\n\n'
    )
    
    print(a, end='\n\n')
    a = 'local var'
    
    print(d, end='\n\n')
    # изменение объекта происходит по ссылке
    d.update({'new_key': 'new_value'})
    # пересоздание объекта осуществляется в локальном пространстве имён
    # d = {'another_key': 'another_value'}
    
    print(
        'текущее пространство имён: взгляд из функции (локальное)', 
        *(f'{k}: {v!r}' for k, v in locals().items() if not k.endswith('__')), 
        sep='\n', end='\n\n'
    )


# >>> print(*globals().items(), sep='\n')
# ('__name__', '__main__')
# ('__doc__', None)
# ('__package__', None)
# ('__loader__', <_frozen_importlib_external.SourceFileLoader object at 0x0000021490EF4A10>)
# ('__spec__', None)
# ('__annotations__', {})
# ('__builtins__', <module 'builtins' (built-in)>)
# ('a', 10)
# ('d', {'key': 'value'})
# ('test', <function test at 0x0000021491392CA0>)


test()
# a: 10
# d: {'key': 'value'}
# test: <function test at 0x000001F8CD673BA0>
# 
# 10
# 
# {'key': 'value'}
# 
# текущее пространство имён: взгляд из функции (локальное)
# param: None
# b: 20

print(
    'текущее пространство имён: взгляд из модуля (глобальное)', 
    *(f'{k}: {v!r}' for k, v in locals().items() if not k.endswith('__')), 
    sep='\n', end='\n\n'
)
# текущее пространство имён: взгляд из модуля (глобальное)
# a: 'local var'
# d: {'key': 'value', 'new_key': 'new_value'}
# test: <function test at 0x000001F8CD673BA0>
