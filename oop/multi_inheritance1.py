class A:
    attr = 'A'


class B:
    attr = 'B'


class C(A, B):
    pass


class D(B, A):
    pass


class E(D):
    pass


# class F(C, D):
#     pass

# приведёт к TypeError: Cannot create a consistent method resolution order (MRO) for bases A, B


# >>> A.__mro__
# (<class '__main__.A'>, <class 'object'>)
# >>>
# >>> B.__mro__
# (<class '__main__.B'>, <class 'object'>)
# >>>
# >>> C.__mro__
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# >>>
# >>> C.attr
# 'A'
# >>>
# >>> D.__mro__
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
# >>>
# >>> D.attr
# 'B'
# >>>
# >>> E.__mro__
# (<class '__main__.E'>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

