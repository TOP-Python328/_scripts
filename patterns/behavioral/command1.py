"""Демонстратор команды."""

from datetime import datetime as dt
from enum import Enum
from pathlib import Path
from sys import path


class Operation(Enum):
    DEPOSIT = 110
    WITHDRAW = 220


class Logger:
    default_log_path: str | Path = Path(path[0]) / 'command1.log'
    
    @classmethod
    def append_log(cls, data: str, log_path: str | Path = None):
        if not log_path:
            log_path = cls.default_log_path
        with open(log_path, 'a', encoding='utf-8') as fileout:
            fileout.write(f'{dt.now():%Y-%m-%d %H:%M:%S} — {data}\n')


class BankAccount:
    """Адресат."""
    overdraft_limit: int = -500
    
    def __init__(self, initial_amount: int = 0):
        self.balance: int = initial_amount
    
    def deposit(self, amount: int) -> None:
        self.balance += amount
    
    def withdraw(self, amount: int) -> bool:
        if (result := self.balance - amount) >= self.overdraft_limit:
            self.balance = result
            return True
        else:
            return False
    
    def __repr__(self):
        return f'{self.balance}'
    
    def __str__(self):
        return f'денег на счёте: {self.balance}₽'


class BACommand:
    """Команда."""
    def __init__(
            self,
            bank_account: BankAccount,
            operation: Operation,
            amount: int
    ):
        self.account = bank_account
        self.operation = operation
        self.amount = amount
        self.success: bool = False
    
    def __log(self, *, undo: bool = False) -> None:
        if undo:
            data = 'UNDO'
        else:
            data = 'OK' if self.success else 'FAIL'
        data += f' — {self.operation.name}: {self.amount}₽ — {self.account!r}₽'
        Logger.append_log(data)
    
    def execute(self) -> None:
        if not self.success:
            if self.operation is Operation.DEPOSIT:
                self.account.deposit(self.amount)
                self.success = True
            elif self.operation is Operation.WITHDRAW:
                self.success = self.account.withdraw(self.amount)
            self.__log()
    
    def undo(self) -> None:
        if self.success:
            if self.operation is Operation.DEPOSIT:
                self.account.withdraw(self.amount)
            elif self.operation is Operation.WITHDRAW:
                self.account.deposit(self.amount)
            self.success = False
            self.__log(undo=True)


# >>> ba = BankAccount(100)
# >>> print(ba)
# денег на счёте: 100₽
# >>>
# >>> c1 = BACommand(ba, Operation.DEPOSIT, 250)
# >>> c1.execute()
# >>> print(ba)
# денег на счёте: 350₽
# >>>
# >>> c2 = BACommand(ba, Operation.WITHDRAW, 500)
# >>> c2.execute()
# >>> print(ba)
# денег на счёте: -150₽
# >>>
# >>> c3 = BACommand(ba, Operation.WITHDRAW, 600)
# >>> c3.execute()
# >>> print(ba)
# денег на счёте: -150₽
# >>>
# >>> c3.undo()
# >>> print(ba)
# денег на счёте: -150₽
# >>>
# >>> c2.undo()
# >>> print(ba)
# денег на счёте: 350₽
# >>>
# >>> c2.undo()
# >>> print(ba)
# денег на счёте: 350₽
# >>>
# >>> c4 = BACommand(ba, Operation.DEPOSIT, 1000)
# >>> c4.execute()
# >>> print(ba)
# денег на счёте: 1350₽
# >>>
# >>> c1.undo()
# >>> print(ba)
# денег на счёте: 1100₽
