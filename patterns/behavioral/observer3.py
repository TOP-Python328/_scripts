"""Демонстратор наблюдателя: наблюдатель с автоматической подпиской и отменой подписки."""

from abc import ABC


class Observers(list):
    """Вызываемый список наблюдателей."""
    def __call__(self, *args, **kwargs):
        for observer in self:
            # вызов наблюдателя
            observer(*args, **kwargs)


class Observable(ABC):
    """Интерфейс наблюдаемого объекта."""
    def __init__(self):
        # список наблюдателей
        self.properties_changed = Observers()


class Person(Observable):
    """Наблюдаемый объект."""
    def __init__(self):
        super().__init__()
        # наблюдаемый атрибут
        self.__age: int = 0
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value: int):
        """Оповещает наблюдателей при изменении значения атрибута."""
        if self.__age == value:
            return
        self.__age = value
        self.properties_changed('age', value)


class TrafficAuthority:
    """Инфраструктура наблюдателя."""
    def __init__(self, person: Person):
        self.person = person
        # автоматическая подписка
        self.person.properties_changed.append(self.age_changed)
    
    def age_changed(self, prop_name: str, prop_value: int):
        """Метод-наблюдатель."""
        if prop_name == 'age':
            if prop_value < 16:
                print('Вам запрещено управлять автомобилем.')
            else:
                print('Вам разрешено управлять автомобилем.')
                # автоматическая отмена подписки
                self.person.properties_changed.remove(self.age_changed)


dima = Person()
gibdd = TrafficAuthority(dima)

for age in range(11, 19):
    print(f'{age = }')
    # генерация события
    dima.age = age
