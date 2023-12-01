"""Демонстратор стратегии: классы в роли стратегий."""

from abc import ABC, abstractmethod
from enum import Enum


class OutputFormat(Enum):
    HTML = 0
    MARKDOWN = 1


class ListStrategy(ABC):
    """Абстрактный класс для стратегий формирования строкового представления текстового списка с использованием различных языков разметки."""
    @abstractmethod
    def start(self, buffer: list[str]):
        pass
    
    @abstractmethod
    def add_item(self, buffer: list[str], item: str):
        pass
    
    @abstractmethod
    def end(self, buffer: list[str]):
        pass


class HTMLStrategy(ListStrategy):
    """Реализация стратегии формирования строкового представления списка с использованием языка разметки HTML."""
    def start(self, buffer: list[str]):
        buffer.append('<ul>')
    
    def add_item(self, buffer: list[str], item: str):
        buffer.append(f'<li>{item}</li>')
    
    def end(self, buffer: list[str]):
        buffer.append('</ul>')


class MarkdownStrategy(ListStrategy):
    """Реализация стратегии формирования строкового представления списка с использованием языка разметки Markdown."""
    def start(self, buffer: list[str]):
        pass
    
    def add_item(self, buffer: list[str], item: str):
        buffer.append(f' * {item}')
    
    def end(self, buffer: list[str]):
        pass


class TextListProcessor:
    def __init__(self, list_strategy: ListStrategy = HTMLStrategy()):
        """
        :param list_strategy: экземпляр класса, определяющего стратегию формирования строкового представления списка с использованием языка разметки
        """
        self.items: list[str] = []
        self.strategy = list_strategy
        self.__output_buffer: list[str] = []
    
    def set_items(self, item1: str, *items: str) -> None:
        self.items = [item1, *items]
        self.__generate_output()
    
    def set_output_format(self, output_format: OutputFormat) -> None:
        if output_format is OutputFormat.HTML:
            self.strategy = HTMLStrategy()
        elif output_format is OutputFormat.MARKDOWN:
            self.strategy = MarkdownStrategy()
        else:
            raise
        self.__generate_output()
    
    def __generate_output(self) -> None:
        self.__output_buffer.clear()
        self.strategy.start(self.__output_buffer)
        for item in self.items:
            self.strategy.add_item(self.__output_buffer, item)
        self.strategy.end(self.__output_buffer)
    
    def __str__(self):
        return '\n'.join(self.__output_buffer)


elements = ('File', 'Edit', 'View', 'Navigate', 'Code', 'Refactor')

tp = TextListProcessor()
tp.set_items(*elements)
print(tp, end='\n\n')

tp.set_output_format(OutputFormat.MARKDOWN)
print(tp, end='\n\n')
