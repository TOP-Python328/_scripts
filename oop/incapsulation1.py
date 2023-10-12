class User:
    def __init__(self, login: str, email: str, password: str):
        # публичный атрибут
        self.login = login
        # "частный" атрибут
        self._email = email
        # "защищённый" атрибут
        self.__password = hash(password)


genndalf = User('GennDALF', 'genn.dalf@ya.ru', 'qwerty')


# >>> genndalf.login
# 'GennDALF'
# >>> genndalf._email
# 'genn.dalf@ya.ru'
# >>> genndalf.__password
# ...
# AttributeError: 'User' object has no attribute '__password'

# для "защищённых" атрибутов работает механим подмены имён (name mangling)
# >>> genndalf.__dict__
# {'login': 'GennDALF', '_email': 'genn.dalf@ya.ru', '_User__password': 7888832499034079137}
# >>>
# >>> genndalf._User__password
# 7888832499034079137

# >>> genndalf.login = 'bugaga'
# >>> genndalf._email = 'fig_tebe@a_ne.email'
# >>> genndalf._User__password = 'ugadai-ka'
# >>> 
# >>> genndalf.__dict__
# {'login': 'bugaga', '_email': 'fig_tebe@a_ne.email', '_User__password': 'ugadai-ka'}


for attr_name, attr_val in genndalf.__dict__.items():
    if not attr_name.startswith(f'_{genndalf.__class__.__name__}'):
        print(f'{attr_name}: {getattr(genndalf, attr_name)!r}')

# login: 'GennDALF'
# _email: 'genn.dalf@ya.ru'


for attr_name in genndalf.__dict__:
    if not attr_name.startswith('_'):
        setattr(genndalf, attr_name, 'новое значение')
        print(f'{attr_name}: {getattr(genndalf, attr_name)!r}')

# login: 'новое значение'

