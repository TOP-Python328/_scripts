class User:
    def __init__(self, login: str, email: str, password: str):
        self.__login = login
        self.__email = email
        self.__password = hash(password)
    
    # геттер без сеттера
    @property
    def login(self) -> str:
        return self.__login
    
    # @property
    # def password(self):
    #     raise NotImplementedError
    
    def password(self, new_password: str) -> None:
        self.__password = hash(new_password)
    
    # сеттер без геттера
    password = property(fset=password)


genndalf = User('GennDALF', 'genn.dalf@ya.ru', 'qwerty')

# >>> print(*User.__dict__.items(), sep='\n')
# ('__module__', '__main__')
# ('__init__', <function User.__init__ at 0x00000191749D2CA0>)
# ('login', <property object at 0x0000019174727F60>)
# ('password', <property object at 0x00000191749FAD90>)
# ('__dict__', <attribute '__dict__' of 'User' objects>)
# ('__weakref__', <attribute '__weakref__' of 'User' objects>)
# ('__doc__', None)


# >>> genndalf.login
# 'GennDALF'
# >>>
# >>> genndalf.login = 'abcde'
# ...
# AttributeError: property 'login' of 'User' object has no setter
# >>>
# >>> genndalf.__dict__
# {'_User__login': 'GennDALF', '_User__email': 'genn.dalf@ya.ru', '_User__password': -914688440947408089}
# >>>
# >>> genndalf.password
# ... 
# AttributeError: property 'password' of 'User' object has no getter
# >>>
# >>> genndalf.password = 'abcdef'
# >>>
# >>> genndalf.__dict__
# {'_User__login': 'GennDALF', '_User__email': 'genn.dalf@ya.ru', '_User__password': 3500237293009877555}

