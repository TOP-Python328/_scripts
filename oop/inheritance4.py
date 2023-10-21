class Person:
    def __init__(
            self, 
            last_name: str, 
            first_name: str, 
            patr_name: str, 
    ):
        self.last_name = last_name
        self.first_name = first_name
        self.patr_name = patr_name


class Employee(Person):
    def __init__(
            self, 
            last_name: str, 
            first_name: str, 
            patr_name: str,
            position: str,
            income: int,
    ):
        # нежелательный вариант — явное обращение к объекту класса
        # Person.__init__(self, last_name, first_name, patr_name)
        
        # предпочтительный вариант — использование прокси-экземпляр
        super().__init__(last_name, first_name, patr_name)
        # print(self.__dict__)
        self.position = position
        self.income = income


# >>> anna = Person('Демидова', 'Анна', 'Олеговна')
# >>>
# >>> anna.__dict__
# {'last_name': 'Демидова', 'first_name': 'Анна', 'patr_name': 'Олеговна'}


# >>> olga = Employee('Балашова', 'Ольга', 'Николаевна', 'специалист кадровой службы', 45000)
# >>>
# >>> olga.__dict__
# {'last_name': 'Балашова', 'first_name': 'Ольга', 'patr_name': 'Николаевна', 'position': 'специалист кадровой службы', 'income': 45000}
