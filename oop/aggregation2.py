from datetime import date, datetime as dt, timedelta as td
from itertools import filterfalse


class Product:
    date_format: str = '%d.%m.%Y'
    
    def __init__(
            self, 
            name: str, 
            days_to_expire: int,
            produced: date | str = date.today(),
    ):
        self.name = name
        if isinstance(produced, str):
            produced = dt.strptime(produced, self.date_format).date()
        self.produced: date = produced
        self.expired: date = produced + td(days=days_to_expire)
    
    def is_expired(self) -> bool:
        return date.today() > self.expired
    
    def __repr__(self):
        return f'<{self.name}: {self.produced:{self.date_format}}—{self.expired:{self.date_format}}>'


class Fridge:
    def __init__(self, *products: Product):
        self.__camera: list[Product] = list(products)
    
    def __iter__(self):
        return iter(self.__camera)
    
    def __len__(self):
        return len(self.__camera)
    
    def __getitem__(self, index: int) -> Product:
        return self.__camera[index]
    
    def __delitem__(self, index: int):
        print('вызов __delitem__()')
        del self.__camera[index]
        
    def __repr__(self):
        products = '\n'.join(repr(pr) for pr in self.__camera)
        return '\n'.join((
            'ХОЛОДИЛЬНИК',
            '-----------',
            products
        ))

    def put(self, product: Product) -> None:
        if isinstance(product, Product):
            self.__camera.append(product)
        else:
            raise TypeError(f"{self.__class__.__name__!r} can contain only 'Product' instances")
    
    def clear_expired(self) -> None:
        self.__camera = list(filterfalse(
            lambda pr: pr.is_expired(),
            self.__camera
        ))


products = (
    Product('молоко', 7, '16.10.2023'),
    Product('морковь', 15, '5.10.2023'),
    Product('хлеб ржаной', 5, date.today()),
    Product('шоколад', 120, '10.04.2023'),
)

minsk = Fridge(*products)

# >>> minsk
# ХОЛОДИЛЬНИК
# -----------
# <молоко: 16.10.2023—23.10.2023>
# <морковь: 05.10.2023—20.10.2023>
# <хлеб ржаной: 18.10.2023—23.10.2023>
# <шоколад: 10.04.2023—08.08.2023>
# >>>
# >>> minsk.clear_expired()
# >>>
# >>> minsk
# ХОЛОДИЛЬНИК
# -----------
# <молоко: 16.10.2023—23.10.2023>
# <морковь: 05.10.2023—20.10.2023>
# <хлеб ржаной: 18.10.2023—23.10.2023>
# >>>
# >>> minsk.put(Product('говяжья лопатка на кости', 2))
# >>>
# >>> minsk
# ХОЛОДИЛЬНИК
# -----------
# <молоко: 16.10.2023—23.10.2023>
# <морковь: 05.10.2023—20.10.2023>
# <хлеб ржаной: 18.10.2023—23.10.2023>
# <говяжья лопатка на кости: 18.10.2023—20.10.2023>
# >>>
# >>> minsk.put('свиная шея б/к')
# ...
# TypeError: 'Fridge' can contain only 'Product' instances
