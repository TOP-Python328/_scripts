"""Демонстратор компоновщика команд."""

from abc import ABC, abstractmethod
from enum import Enum
from dataclasses import dataclass


class Operation(Enum):
    DEPOSIT = 0
    WITHDRAW = 1


class BankAccount:
    """Адресат команд."""
    overdraft_limit: int = -500

    def __init__(self, start_balance: int = 0):
        self._balance = start_balance

    def deposit(self, amount: int) -> None:
        self._balance += amount

    def withdraw(self, amount: int) -> bool:
        if self._balance - amount >= self.overdraft_limit:
            self._balance -= amount
            return True
        return False

    def __str__(self):
        return f'Balance: {self._balance}'



class Command(ABC):
    """Базовый класс команд для различных действий."""
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


@dataclass
class BACommand(Command):
    """Одна команда."""
    account: BankAccount
    action: Operation
    amount: int
    success: bool = False

    def execute(self):
        if self.action is Operation.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
        elif self.action is Operation.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

    def undo(self):
        if self.success:
            if self.action is Operation.DEPOSIT:
                self.account.withdraw(self.amount)
            elif self.action is Operation.WITHDRAW:
                self.account.deposit(self.amount)
            self.success = False


class CompositeBACommand(Command, list):
    """Список команд."""
    def __init__(self, *commands: Command):
        super().__init__()
        for command in commands:
            self.append(command)

    def execute(self):
        for command in self:
            command.execute()

    def undo(self):
        for command in self[::-1]:
            command.undo()


ba1 = BankAccount(100)
print(f'ba1 {ba1}\n')

ccmds = CompositeBACommand(
    BACommand(ba1, Operation.DEPOSIT, 100),
    BACommand(ba1, Operation.WITHDRAW, 120)
)
ccmds.execute()
print(f'ba1 {ba1}\n')

ccmds.undo()
print(f'ba1 {ba1}\n')

