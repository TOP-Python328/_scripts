class Parent1UserError(Exception):
    pass

class Child1UserError(Parent1UserError):
    pass

class Child2UserError(Parent1UserError):
    pass

class SubChildUserError(Child2UserError):
    pass

class Parent2UserError(Exception):
    pass


try:
    # raise Parent1UserError
    # raise Child1UserError
    # raise Child2UserError
    raise SubChildUserError
    # raise Parent2UserError
except Parent1UserError:
    print('except Parent1UserError')


try:
    raise Parent1UserError
except Child2UserError:
    print('except Child2UserError')
