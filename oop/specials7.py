class Battery:
    def __init__(self, capacity: int):
        self.charge: int = 0
        self.capacity = capacity
    
    # self + other
    def __add__(self, other: int):
        return self.__iadd__(other)
    
    # other + self
    def __radd__(self, other: int):
        # return self + other
        return self.__iadd__(other)
    
    # self += other
    def __iadd__(self, other: int):
        if isinstance(other, int):
            res = self.charge + other
            res = self.capacity if res >= self.capacity else res
            self.charge = res
            return self
        else:
            raise TypeError
    
    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.charge}/{self.capacity}>'


lc2032 = Battery(10)

# >>> lc2032 + 5
# <Battery: 5/10>
# >>>
# >>> 3 + lc2032
# <Battery: 8/10>
# >>>
# >>> lc2032 += 6
# >>> lc2032
# <Battery: 10/10>
