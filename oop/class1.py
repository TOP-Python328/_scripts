class Test:
    """
    Демонстрационный класс.
    """
    attr1 = 'атрибут класса'


# объект класса
# >>> Test
# <class '__main__.Test'>

# внутреннее пространство имён объекта класса
# >>> Test.__dict__
# mappingproxy({'__module__': '__main__', '__doc__': '\n    Демонстрационный класс.\n    ', 'attr1': 'атрибут класса', '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>})

# >>> Test.attr1
# 'атрибут класса'


# создание объекта экземпляра
instance = Test()

# >>> instance
# <__main__.Test object at 0x00000207B8A20990>

# ссылка на объект класса, от которого создан данный экземпляр
# >>> instance.__class__
# <class '__main__.Test'>
# >>> 
# >>> Test is instance.__class__ is type(instance)
# True

# внутреннее пространство имён объекта экземпляра
# >>> instance.__dict__
# {}

# область видимости экземпляра расширяется до внутреннего пространства имён класса
# >>> instance.attr1
# 'атрибут класса'


# добавление атрибута экземпляра
instance.attr2 = 'атрибут экземпляра'

# >>> instance.__dict__
# {'attr2': 'атрибут экземпляра'}

# добавление ещё одного атрибута экземпляра
instance.attr1 = 'атрибут экземпляра, затеняющий атрибут класса'

# внутреннее пространство имён класса не изменилось
# >>> Test.__dict__
# mappingproxy({'__module__': '__main__', '__doc__': '\n    Демонстрационный класс.\n    ', 'attr1': 'атрибут класса', '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>})

# >>> instance.__dict__
# {'attr2': 'атрибут экземпляра', 'attr1': 'атрибут экземпляра, затеняющий атрибут класса'}

# >>> instance.attr1
# 'атрибут экземпляра, затеняющий атрибут класса'
# >>>
# >>> instance.__class__.attr1
# 'атрибут класса'
# >>>
# >>> Test.attr1 = 'новое значение'
# >>>
# >>> instance.__class__.attr1
# 'новое значение'

