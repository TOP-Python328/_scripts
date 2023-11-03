from typing import Literal


class Cat:
    def __init__(self, country: Literal['ru', 'jp']):
        self.native = country
    
    def make_sound(self):
        match self.native:
            case 'ru':
                sound = 'мяу'
            case 'jp':
                sound = 'няя'
        print(sound)


class Dog:
    @staticmethod
    def make_sound():
        print('гав')


class Snake:
    @staticmethod
    def make_sound():
        print('шшш')


class Fish:
    @staticmethod
    def make_sound():
        print('...')


zoo = (Cat('ru'), Dog(), Cat('jp'), Snake(), Cat('ru'), Fish(), Fish())
for animal in zoo:
    animal.make_sound()
