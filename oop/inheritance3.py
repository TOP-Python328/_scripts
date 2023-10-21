class Proteus:
    @staticmethod
    def move():
        return 'движение'
    
    @staticmethod
    def eat():
        return 'питание'
    
    @staticmethod
    def reproduce():
        return 'размножение'


class Fish(Proteus):
    @staticmethod
    def breath():
        return 'дыхание'


class Reptile(Fish):
    @staticmethod
    def hide():
        return 'скрытность'


class Bird(Reptile):
    @staticmethod
    def fly():
        return 'полёт'


class Mammal(Reptile):
    @staticmethod
    def care():
        return 'забота'


class Human(Mammal):
    @staticmethod
    def speak():
        return 'речь'


ivan = Human()

# >>> ivan.speak()
# 'речь'
# >>> ivan.care()
# 'забота'
# >>> ivan.fly()
# ...
# AttributeError: 'Human' object has no attribute 'fly'
# >>> ivan.hide()
# 'скрытность'
# >>> ivan.breath()
# 'дыхание'
# >>> ivan.reproduce()
# 'размножение'
# >>> ivan.eat()
# 'питание'
# >>> ivan.move()
# 'движение'

# >>> print(*ivan.__class__.__mro__, sep='\n')
# <class '__main__.Human'>
# <class '__main__.Mammal'>
# <class '__main__.Reptile'>
# <class '__main__.Fish'>
# <class '__main__.Proteus'>
# <class 'object'>


liza = Reptile()

# >>> liza.move()
# 'движение'
# >>> liza.eat()
# 'питание'
# >>> liza.reproduce()
# 'размножение'
# >>> liza.hide()
# 'скрытность'
# >>> liza.breath()
# 'дыхание'
# >>> liza.fly()
# ...
# AttributeError: 'Reptile' object has no attribute 'fly'
# >>> liza.care()
# ...
# AttributeError: 'Reptile' object has no attribute 'care'
# >>> liza.speak()
# ...
# AttributeError: 'Reptile' object has no attribute 'speak'

# >>> print(*liza.__class__.__mro__, sep='\n')
# <class '__main__.Reptile'>
# <class '__main__.Fish'>
# <class '__main__.Proteus'>
# <class 'object'>

