class Presentation1:
    def __repr__(self):
        return 'repr presented'


class Presentation2:
    def __repr__(self):
        return 'repr presented'
    
    def __str__(self):
        return 'str presented'


class Presentation3:
    def __str__(self):
        return 'str presented'


pr1 = Presentation1()
pr2 = Presentation2()
pr3 = Presentation3()

# >>> pr1
# repr presented
# >>>
# >>> pr1.__repr__()
# 'repr presented'
# >>>
# >>> pr1.__str__()
# 'repr presented'
# >>>
# >>> print(pr1)
# repr presented

# >>> pr2
# repr presented
# >>>
# >>> print(pr2)
# str presented

# >>> pr3
# <__main__.Presentation3 object at 0x000002B3F1091150>
# >>>
# >>> print(pr3)
# str presented
