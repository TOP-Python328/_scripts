class Person:
    
    class Sex:
        M = 'мужской'
        F = 'женский'
    
    def __init__(self, family: str, name: str, sex: str):
        self.last_name = family
        self.first_name = name
        self.sex = sex


ilya = Person('Денисов', 'Илья', Person.Sex.M)
liza = Person('Макарова', 'Елизавета', Person.Sex.F)

for pers in (ilya, liza):
    if pers.sex == Person.Sex.M:
        print('мужик')
    elif pers.sex == Person.Sex.F:
        print('девушка')
    else:
        print('нечто')

