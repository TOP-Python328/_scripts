class Square:
    def __init__(self, side: float):
        self.__side = side
        self.__area = side**2
    
    # геттер
    @property
    def side(self) -> float:
        print('вызов геттера')
        return round(self.__side, 1)
    
    # сеттер
    @side.setter
    def side(self, new_side: float) -> None:
        print('вызов сеттера')
        self.__side = new_side
        self.__area = new_side**2
    
    # геттер
    @property
    def area(self) -> float:
        print('вызов геттера')
        return round(self.__area, 1)
    
    # сеттер
    @area.setter
    def area(self, new_area: float) -> None:
        print('вызов сеттера')
        self.__side = new_area**0.5
        self.__area = new_area


sq1 = Square(5.37)

# >>> sq1.side
# вызов геттера
# 5.4
# >>> sq1.side = 6.02
# вызов сеттера
# >>>
# >>> sq1.__dict__
# {'_Square__side': 6.02, '_Square__area': 36.240399999999994}


# >>> print(*Square.__dict__.items(), sep='\n')
# ('__module__', '__main__')
# ('__init__', <function Square.__init__ at 0x0000013F0B6F2CA0>)
# ('side', <property object at 0x0000013F0B71ADE0>)
# ('area', <property object at 0x0000013F0B71AE80>)
# ('__dict__', <attribute '__dict__' of 'Square' objects>)
# ('__weakref__', <attribute '__weakref__' of 'Square' objects>)
# ('__doc__', None)

