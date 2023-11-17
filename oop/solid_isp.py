"""Interface Segregation Principle — Принцип Разделения Интерфейсов"""

from abc import ABC, abstractmethod


class MultiFunctionalDevice(ABC):
    @abstractmethod
    def print(self):
        pass
    
    # нарушение ISP — несколько интерфейсов объединены в одном классе
    
    @abstractmethod
    def scan(self):
        pass
    
    @abstractmethod
    def fax(self):
        pass


class XeroxM100(MultiFunctionalDevice):
    def print(self):
        return 'печать'
    
    def scan(self):
        return 'сканирование'
    
    def fax(self):
        return 'получение факса'


class BrotherHL5250(MultiFunctionalDevice):
    def print(self):
        return 'печать'
    
    # лишние атрибуты
    
    def scan(self):
        raise NotImplementedError
    
    def fax(self):
        raise NotImplementedError


# решение — предоставить раздельные интерфейсы

class Printer(ABC):
    @abstractmethod
    def print(self):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self):
        pass


class Fax(ABC):
    @abstractmethod
    def fax(self):
        pass


class XeroxM100(Printer, Scanner, Fax):
    def print(self):
        return 'печать'
    
    def scan(self):
        return 'сканирование'
    
    def fax(self):
        return 'получение факса'


class BrotherHL5250(Printer):
    def print(self):
        return 'печать'

