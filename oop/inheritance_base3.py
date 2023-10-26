from collections.abc import Iterable


class FixedList(list):
    def __init__(self, max_length: int, iterable: Iterable = ()):
        super().__init__(iterable)
        self.__max_length = max_length
    
    def append(self, element):
        if len(self) == self.__max_length:
            del self[0]
        super().append(element)
    
    def extend(self, iterable: Iterable):
        it_len = len(iterable)
        if it_len > self.__max_length:
            raise ValueError('...')
        diff = len(self) + it_len - self.__max_length
        if diff > 0:
            del self[:diff]
        super().extend(iterable)
    
    def __iadd__(self, other: list):
        self.extend(other)
        return self


# >>> numbers = FixedList(5)
# >>>
# >>> numbers
# []
# >>> numbers.append(1)
# >>> numbers
# [1]
# >>> numbers.append(2)
# >>> numbers
# [1, 2]
# >>> numbers.append(3)
# >>> numbers
# [1, 2, 3]
# >>> numbers.append(4)
# >>> numbers
# [1, 2, 3, 4]
# >>> numbers.append(5)
# >>> numbers
# [1, 2, 3, 4, 5]
# >>> numbers.append(6)
# >>> numbers
# [2, 3, 4, 5, 6]

# >>> numbers = FixedList(4)
# >>>
# >>> numbers.extend([1, 2])
# >>> numbers
# [1, 2]
# >>>
# >>> numbers.extend([3, 4])
# >>> numbers
# [1, 2, 3, 4]
# >>>
# >>> numbers.extend([5, 6])
# >>> numbers
# [3, 4, 5, 6]
# >>> numbers.extend(range(7, 50))
# ...
# ValueError: ...

# >>> numbers = FixedList(4, range(1, 4))
# >>> numbers
# [1, 2, 3]
# >>> id(numbers)
# 2802801652704
# >>>
# >>> numbers += [10, 20, 30]
# >>> numbers
# [3, 10, 20, 30]
# >>> id(numbers)
# 2802801652704

