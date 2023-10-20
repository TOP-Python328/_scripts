class A:
    def __init__(self):
        self.attr = 'атрибут класса А'


class B:
    def __init__(self, associated_object: A):
        self.associated = associated_object


a = A()
b = B(a)

