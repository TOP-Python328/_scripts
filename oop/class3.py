class Person:
    # специальный метод конструктор — вызывается во время создания экземпляра
    def __init__(self, family: str, name: str):
        # добавление атрибутов экземпляра
        self.last_name = family
        self.first_name = name


ivan = Person('Фекистов', 'Иван')
anna = Person('Дунаевская', 'Анна')

# >>> ivan.__dict__
# {'last_name': 'Фекистов', 'first_name': 'Иван'}

# >>> anna.__dict__
# {'last_name': 'Дунаевская', 'first_name': 'Анна'}

