class Square:
    def __init__(self, side: float):
        self.side = side
        self.area = side**2
    
    # классический геттер
    def get_side(self) -> float:
        return self.side
    
    # классический сеттер
    def set_side(self, new_side: float) -> None:
        self.side = new_side
        self.area = new_side**2
    
    # классический геттер
    def get_area(self) -> float:
        return self.area
    
    # классический сеттер
    def set_area(self, new_area: float) -> None:
        self.side = new_area**0.5
        self.area = new_area


sq1 = Square(5)

# >>> sq1.side
# 5
# >>> sq1.area
# 25
# >>>
# >>> sq1.side = 10
# >>> sq1.side
# 10
# рассогласование атрибутов
# >>> sq1.area
# 25

# >>> sq1.set_side(12)
# >>> sq1.side
# 12
# >>> sq1.area
# 144
# >>>
# >>> sq1.set_area(49)
# >>> sq1.side
# 7.0
# >>> sq1.area
# 49

