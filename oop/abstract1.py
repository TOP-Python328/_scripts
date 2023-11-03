from abc import ABC, abstractmethod


class Test(ABC):
    @abstractmethod
    def method_to_be_released_in_subclasses():
        pass


# >>> ABC
# <class 'abc.ABC'>
# >>>
# >>> type(ABC)
# <class 'abc.ABCMeta'>
# >>>
# >>> Test
# <class '__main__.Test'>
# >>>
# >>> Test.__mro__
# (<class '__main__.Test'>, <class 'abc.ABC'>, <class 'object'>)


# до объявления абстрактного метода
# >>> Test()
# <__main__.Test object at 0x00000220C10CEA10>


# после объявления абстрактного метода
# >>> Test()
# ...
# TypeError: Can't instantiate abstract class Test with abstract method method_to_be_released_in_subclasses


class SubTest(Test):
    def method_to_be_released_in_subclasses():
        print('just do it')
        


# до переопределния унаследованного абстрактного метода
# >>> SubTest()
# ...
# TypeError: Can't instantiate abstract class SubTest with abstract method method_to_be_released_in_subclasses


# после переопределния унаследованного абстрактного метода
# >>> SubTest()
# <__main__.SubTest object at 0x000002631B130D50>


