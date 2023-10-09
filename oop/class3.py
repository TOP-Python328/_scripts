class Person:
    # специальный метод конструктор — вызывается во время создания экземпляра
    def __init__(self, family: str, name: str) -> None:
        # добавление атрибутов экземпляра
        self.last_name = family
        self.first_name = name


ivan = Person('Фекистов', 'Иван')
anna = Person('Дунаевская', 'Анна')


# при вызове объекта класса class_ выполняется метод __call__(), определённый в метаклассе type:
# def __call__(class_, *args, **kwargs) -> 'instance':
#     ...
#     instance = class_.__new__(class_, *args, **kwargs)
#     ...
#     instance.__init__(*args, **kwargs)
#     ...
#     return instance

# >>> ivan.__dict__
# {'last_name': 'Фекистов', 'first_name': 'Иван'}

# >>> anna.__dict__
# {'last_name': 'Дунаевская', 'first_name': 'Анна'}

