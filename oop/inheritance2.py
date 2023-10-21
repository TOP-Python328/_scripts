from pprint import pprint


class Parent:
    attr = 'parent value'


class Child(Parent):
    # переопределение родительского атрибута в дочернем классе
    attr = 'child value'


# >>> Parent.attr
# 'parent value'
# >>>
# >>> Child.attr
# 'child value'

