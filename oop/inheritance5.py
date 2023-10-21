class Vehicle:
    wheels = 4
    
    def __init__(self, average_speed: int):
        self.speed = average_speed

    def move(self) -> str:
        return f'{self.__class__.__name__} moves on the ground with average speed of {self.speed} km/h'


class Bicycle(Vehicle):
    wheels = 2


class Car(Vehicle):
    pass


class Train(Vehicle):
    wheels = 16

    def move(self) -> str:
        return super().move().replace('on the ground', 'along railroads')


class Aircraft(Vehicle):
    wheels = 6
    
    # нарушение Принципа Подстановки Лисков
    def __init__(self, average_ground_speed: int, average_air_speed: int):
        self.ground_speed = average_ground_speed
        self.air_speed = average_air_speed

    def move(self) -> str:
        return f'On the ground {self.__class__.__name__} moves with average speed of {self.ground_speed} km/h while in the air it flies with average speed of {self.air_speed} km/h'


def sort_by_speed(*vehicles: Vehicle) -> list[Vehicle]:
    return sorted(
        vehicles,
        key=lambda v: v.speed
    )


sputnik = Bicycle(16)
volga = Car(60)
sapsan = Train(250)
ssj_100 = Aircraft(50, 700)

# >>> sort_by_speed(ssj_100, sapsan, sputnik, volga)
# ...
# AttributeError: 'Aircraft' object has no attribute 'speed'

# >>> sort_by_speed(sapsan, sputnik, volga)
# [<__main__.Bicycle object at 0x0000021CB00A1350>, <__main__.Car object at 0x0000021CB00A0B50>, <__main__.Train object at 0x0000021CB00A1010>]
