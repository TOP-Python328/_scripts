class A:
    def __init__(self):
        print(f'экземпляр {self.__class__.__name__}: конструктор А')
        self.attr = 'атрибут A'


class B:
    def __init__(self):
        print(f'экземпляр {self.__class__.__name__}: конструктор B')
        self.attr = 'атрибут B'


class C(A, B):
    def __init__(self):
        print(f'экземпляр {self.__class__.__name__}: конструктор C')
        super().__init__()


# >>> C.__mro__
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# >>>
# >>> c = C()
# экземпляр C: конструктор C
# экземпляр C: конструктор А
# >>>
# >>> c.attr
# 'атрибут A'


class D(A, B):
    def __init__(self):
        print(f'экземпляр {self.__class__.__name__}: конструктор D')
        super(A, self).__init__()


# >>> D.__mro__
# (<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# >>>
# >>> d = D()
# экземпляр D: конструктор D
# экземпляр D: конструктор B
# >>>
# >>> d.attr
# 'атрибут B'


class E:
    pass


class F(E, C, D):
    pass


# >>> print(*F.__mro__, sep='\n')
# <class '__main__.F'>
# <class '__main__.E'>
# <class '__main__.C'>
# <class '__main__.D'>
# <class '__main__.A'>
# <class '__main__.B'>
# <class 'object'>
# >>>
# >>> f = F()
# экземпляр F: конструктор C
# экземпляр F: конструктор D
# экземпляр F: конструктор B
# >>>
# >>> f.attr
# 'атрибут B'

