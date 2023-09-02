def external():
    var1 = 10
    
    def internal():
        nonlocal var1
        var1 = 'изменили!'
        var2 = 20
        print(
            'локальное пространство имён internal()', 
            *(f'{k}: {v!r}' for k, v in locals().items()), 
            sep='\n', end='\n\n'
        )
    
    internal()
    print(
        'локальное пространство имён external()', 
        *(f'{k}: {v!r}' for k, v in locals().items()), 
        sep='\n', end='\n\n'
    )


# >>> external()
# локальное пространство имён internal()
# var2: 20
# var1: 'изменили!'
# 
# локальное пространство имён external()
# internal: <function external.<locals>.internal at 0x000002350FA1F920>
# var1: 'изменили!'
