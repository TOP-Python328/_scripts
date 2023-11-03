from abc import ABC, abstractmethod


class MapObject(ABC):
    @abstractmethod
    def info(self) -> str:
        pass


class Building(MapObject):
    def __init__(self, address: str, organizations: list[str]):
        self.address = address
        self.organizations = organizations
    
    def info(self, full: bool = False) -> str:
        result = self.address
        if full:
            result += '\n' + '\n'.join(self.organizations)
        return result


class TransportObject(MapObject):
    def __init__(self, name: str, routes: list[str]):
        self.name = name
        self.routes = routes
    
    def info(self) -> str:
        return f"{self.name}\n{', '.join(self.routes)}"


b1 = Building(
    'улица Куйбышева, 67, Екатеринбург, Свердловская область, 620026',
    ['Сбербанк', 'Сбер банкомат', 'Домклик']
)
t1 = TransportObject(
    'улица Белинского',
    ['3', '4', '6', '10', '14', '20', '21']
)

for obj in (b1, t1):
    print(obj.info(), end='\n\n')

print(b1.info(full=True), end='\n\n')
