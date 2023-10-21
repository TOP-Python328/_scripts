from pprint import pprint


# родительский класс / базовый класс / надкласс / superclass
class Parent:
    parent_attr = 'parent value'


# дочерний класс / производный класс / подкласс / subclass
class Child(Parent):
    child_attr = 'child value'


# внутреннее пространство имён родительского класса
# >>> pprint(Parent.__dict__, sort_dicts=False)
# mappingproxy({'__module__': '__main__',
#               'parent_attr': 'parent value',
#               '__dict__': <attribute '__dict__' of 'Parent' objects>,
#               '__weakref__': <attribute '__weakref__' of 'Parent' objects>,
#               '__doc__': None})

# внутреннее пространство имён дочернего класса
# >>> pprint(Child.__dict__, sort_dicts=False)
# mappingproxy({'__module__': '__main__',
#               'child_attr': 'child value',
#               '__doc__': None})

# при отсутствии запрошенного атрибута во внутреннем пространстве имён область видимости расширяется до родительского класса
# >>> Child.parent_attr
# 'parent value'

# область видимости, расширенная до пространства имён родительского класса
# >>> attrs = [
# ...    attr 
# ...    for attr in dir(Child) 
# ...    if attr in Child.__dict__ or attr in Parent.__dict__
# ... ]
# >>> pprint(attrs, sort_dicts=False)
# ['__dict__',
#  '__doc__',
#  '__module__',
#  '__weakref__',
#  'child_attr',
#  'parent_attr']


# mro — method resolution order (порядок разрешения методов)
# >>> Parent.__mro__
# (<class '__main__.Parent'>, <class 'object'>)
# >>>
# >>> Child.__mro__
# (<class '__main__.Child'>, <class '__main__.Parent'>, <class 'object'>)


# внутреннее пространство имён корневого класса
# >>> pprint(object.__dict__, sort_dicts=False)
# mappingproxy({'__new__': <built-in method __new__ of type object at 0x00007FF805CC8DF0>,
#               '__repr__': <slot wrapper '__repr__' of 'object' objects>,
#               '__hash__': <slot wrapper '__hash__' of 'object' objects>,
#               '__str__': <slot wrapper '__str__' of 'object' objects>,
#               '__getattribute__': <slot wrapper '__getattribute__' of 'object' objects>,
#               '__setattr__': <slot wrapper '__setattr__' of 'object' objects>,
#               '__delattr__': <slot wrapper '__delattr__' of 'object' objects>,
#               '__lt__': <slot wrapper '__lt__' of 'object' objects>,
#               '__le__': <slot wrapper '__le__' of 'object' objects>,
#               '__eq__': <slot wrapper '__eq__' of 'object' objects>,
#               '__ne__': <slot wrapper '__ne__' of 'object' objects>,
#               '__gt__': <slot wrapper '__gt__' of 'object' objects>,
#               '__ge__': <slot wrapper '__ge__' of 'object' objects>,
#               '__init__': <slot wrapper '__init__' of 'object' objects>,
#               '__reduce_ex__': <method '__reduce_ex__' of 'object' objects>,
#               '__reduce__': <method '__reduce__' of 'object' objects>,
#               '__getstate__': <method '__getstate__' of 'object' objects>,
#               '__subclasshook__': <method '__subclasshook__' of 'object' objects>,
#               '__init_subclass__': <method '__init_subclass__' of 'object' objects>,
#               '__format__': <method '__format__' of 'object' objects>,
#               '__sizeof__': <method '__sizeof__' of 'object' objects>,
#               '__dir__': <method '__dir__' of 'object' objects>,
#               '__class__': <attribute '__class__' of 'object' objects>,
#               '__doc__': 'The base class of the class hierarchy.\n'
#                          '\n'
#                          'When called, it accepts no arguments and returns a '
#                          'new featureless\n'
#                          'instance that has no instance attributes and cannot '
#                          'be given any.\n'})


