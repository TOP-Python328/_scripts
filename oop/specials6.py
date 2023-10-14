class Fridge:
    def __init__(self, *products: str):
        self.__camera: list[str] = list(filter(
            lambda p: isinstance(p, str), 
            products
        ))
    
    def __iter__(self):
        return iter(self.__camera)
    
    def __len__(self):
        return len(self.__camera)
    
    def __getitem__(self, index: int) -> str:
        return self.__camera[index]
    
    def __delitem__(self, index: int):
        print('вызов __delitem__()')
        del self.__camera[index]
    
    def put(self, product: str):
        if isinstance(product, str):
            self.__camera.append(product)
        # else:
        #     raise TypeError
    
    def __repr__(self):
        return '\n'.join(self.__camera)


minsk = Fridge(
    'молоко',
    'сосиски',
    'суп',
    148
)

# >>> minsk
# молоко
# сосиски
# суп
# >>> minsk[0]
# 'молоко'
# >>> minsk[2]
# 'суп'
# >>> minsk[5]
# ...
# IndexError: list index out of range
# >>> minsk['asd']
# ...
# TypeError: list indices must be integers or slices, not str
# >>> 
# >>> del minsk[1]
# вызов __delitem__()
# >>> 
# >>> minsk
# молоко
# суп

