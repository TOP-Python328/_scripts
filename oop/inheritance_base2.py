from datetime import date, datetime as dt, timedelta as td


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


class Fridge(list):
    def __repr__(self):
        products = '\n'.join(repr(pr) for pr in self)
        return '\n'.join((
            'ХОЛОДИЛЬНИК',
            '-----------',
            products
        ))

    def append(self, product: Product):
        if isinstance(product, Product):
            super().append(product)
        else:
            raise TypeError(f"{self.__class__.__name__!r} can contain only 'Product' instances")
    
    def clear_expired(self) -> None:
        for pr in [pr for pr in self if pr.is_expired()]:
            self.remove(pr)

    # def clear_expired(self) -> None:
    #     for i in range(len(self)-1, -1, -1):
    #         if self[i].is_expired():
    #             del self[i]



products = (
    Product('молоко', 7, '16.10.2023'),
    Product('морковь', 15, '5.10.2023'),
    Product('хлеб ржаной', 5, date.today()),
    Product('шоколад', 120, '10.04.2023'),
)

minsk = Fridge(products)

# >>> minsk
# ХОЛОДИЛЬНИК
# -----------
# <молоко: 16.10.2023—23.10.2023>
# <морковь: 05.10.2023—20.10.2023>
# <хлеб ржаной: 25.10.2023—30.10.2023>
# <шоколад: 10.04.2023—08.08.2023>
# >>>
# >>> minsk.clear_expired()
# >>>
# >>> minsk
# ХОЛОДИЛЬНИК
# -----------
# <хлеб ржаной: 25.10.2023—30.10.2023>

