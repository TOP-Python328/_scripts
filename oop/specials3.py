class Person:
    def __init__(self, last_name: str, first_name: str, patr_name: str):
        self.last_name = last_name
        self.first_name = first_name
        self.patr_name = patr_name
    
    def __format__(self, format_spec: str):
        if format_spec == 'fio':
            return f'{self.last_name} {self.first_name} {self.patr_name}'
        elif format_spec == 'io':
            return f'{self.first_name} {self.patr_name}'
        elif format_spec == 'in_f':
            return f'{self.first_name[0]}. {self.patr_name[0]}. {self.last_name}'
        elif format_spec == 'in_l':
            return f'{self.last_name} {self.first_name[0]}. {self.patr_name[0]}.'
        else:
            raise ValueError(f'Invalid format specifier {format_spec!r} for object of type {self.__class__.__name__!r}')


ivan = Person('Разумов', 'Иван', 'Олегович')

# >>> f'{ivan}'
# ...
# ValueError: Invalid format specifier '' for object of type 'Person'
# >>>
# >>> f'{ivan:fio}'
# 'Разумов Иван Олегович'
# >>>
# >>> f'{ivan:io}'
# 'Иван Олегович'
# >>>
# >>> f'{ivan:in_f}'
# 'И. О. Разумов'
# >>>
# >>> f'{ivan:in_l}'
# 'Разумов И. О.'
