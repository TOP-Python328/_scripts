"""
Приложение Сапёр — с использованием MVC.
"""

from dataclasses import dataclass
from enum import Enum
from random import randrange as rr
from typing import Optional, Self

from tkinter import Button, Frame, Label, Tk, Spinbox, StringVar
from tkinter.messagebox import showinfo
from tkinter.constants import BOTTOM, LEFT, RIGHT, SUNKEN, X


# переменные для аннотации
CellsMatrix = list[list['Cell']]
ButtonsBoard = list[list[Button]]


class States(Enum):
    OPENED = 'o'
    CLOSED = ''
    FLAGGED = '🚩'
    QUESTIONED = '?'
    
    @classmethod
    def cycling(cls) -> list[Self]:
        tmp = list(cls)
        tmp.remove(cls.OPENED)
        return tmp


@dataclass
class Cell:
    """
    Описывает сущность одной клетки игрового поля.
    """
    row: int
    column: int
    state: States = States.CLOSED
    mined: bool = False
    counter: int = 0
    
    __cycling_states = States.cycling()
    def next_state(self):
        """Циклически переключает состояния клетки."""
        if self.state is not States.OPENED:
            i = self.__cycling_states.index(self.state)
            self.state = self.__cycling_states[(i+1) % 3]
    
    def open(self):
        """Переключает клетку в состояние 'открыто'."""
        if self.state is not States.OPENED:
            self.state = States.OPENED


MIN_ROWS = 5
MAX_ROWS = 30

MIN_COLUMNS = 5
MAX_COLUMNS = 30

MIN_MINES = 10
MAX_MINES = 800


class Matrix:
    def __init__(self):
        self.create_matrix()
    
    def create_matrix(
            self,
            rows: int = 10,
            columns: int = 10,
            mines: int = 20
    ) -> None:
        """Инициализирует клетки нового игрового поля.
        
        :param rows: количество строк игрового поля
        :param columns: количество столбцов игрового поля
        :param mines: количество мин на игровом поле
        """
        if MIN_ROWS <= rows <= MAX_ROWS:
            self.rows = rows
        if MIN_COLUMNS <= columns <= MAX_COLUMNS:
            self.columns = columns
        if MIN_MINES <= mines <= MAX_MINES and mines < self.rows*self.columns:
            self.mines = mines
        
        self.matrix: CellsMatrix = [
            [Cell(i, j) for j in range(self.columns)]
            for i in range(self.rows)
        ]
        self.game_over: bool = False
        self.first_step: bool = True
    
    def _generate_mines(self) -> None:
        """Располагает заданное количество мин на случайных клетках игрового поля."""
        for _ in range(self.mines):
            while True:
                i = rr(self.rows)
                j = rr(self.columns)
                cell = self.matrix[i][j]
                if not cell.mined and cell.state is not States.OPENED:
                    cell.mined = True
                    break
    
    def is_win(self) -> bool:
        """Проверяет, достигнут ли выигрыш."""
        for row in self.matrix:
            for cell in row:
                opened_or_flagged = cell.state is States.OPENED or cell.state is States.FLAGGED
                if not cell.mined and not opened_or_flagged:
                    return False
        return True
    
    def is_game_over(self) -> bool:
        """Проверяет, случился ли проигрыш."""
        return self.game_over
    
    def cell_cycle_state(self, row: int, column: int) -> None:
        """Переключает отметку на клетке."""
        self.matrix[row][column].next_state()
    
    def get_cell(self, row: int, column: int) -> Optional[Cell]:
        """Возвращает клетку по заданным индексам, если индексы находятся в заданном диапазоне, иначе None."""
        if 0 <= row < self.rows and 0 <= column < self.columns:
            return self.matrix[row][column]
        return None
    
    def _get_cell_neighbours(self, row: int, column: int) -> list[Cell]:
        """Возвращает список клеток, соседних с клеткой, заданной переданными индексами."""
        neighbours = []
        for i in range(row-1, row+2):
            neighbours.append(self.get_cell(i, column-1))
            if i != row:
                neighbours += [self.get_cell(i, column)]
            neighbours += [self.get_cell(i, column+1)]
        return [cell for cell in neighbours if cell is not None]
    
    def _get_mines_around_cell(self, row: int, column: int) -> int:
        """Подсчитывает и возвращает количество заминированных клеток рядом с клеткой, заданной переданными индексами."""
        neighbours = self._get_cell_neighbours(row, column)
        return sum(cell.mined for cell in neighbours)
    
    def open_cell(self, row: int, column: int) -> None:
        """Открывает клетку, проверяет мину, подсчитывает количество мин рядом с открытой, рекурсивно открывает соседние пустые клетки."""
        cell = self.get_cell(row, column)
        if cell is None:
            return
        
        cell.open()
        
        if cell.mined:
            self.game_over = True
            return
        
        if self.first_step:
            self.first_step = False
            self._generate_mines()
        
        cell.counter = self._get_mines_around_cell(row, column)
        
        if cell.counter == 0:
            neighbours = self._get_cell_neighbours(row, column)
            for n_cell in neighbours:
                if n_cell.state is States.CLOSED:
                    self.open_cell(n_cell.row, n_cell.column)


class GUI(Frame):
    def __init__(
            self,
            model_obj: 'Matrix',
            controller_obj: 'Game',
            parent=None
    ):
        super().__init__(parent)
        
        self.model = model_obj
        self.controller = controller_obj
        self.controller.set_view(self)
        
        self.rows = StringVar(value=str(self.model.rows))
        self.columns = StringVar(value=str(self.model.columns))
        self.mines = StringVar(value=str(self.model.mines))
        
        self.create_board()
        self.create_panel()
    
    def create_board(self) -> None:
        try:
            self.board.pack_forget()
            self.board.destroy()
        except AttributeError:
            pass
        else:
            self.rows.set(str(self.model.rows))
            self.columns.set(str(self.model.columns))
            self.mines.set(str(self.model.mines))
        
        self.board = Frame(self)
        self.board.pack()
        
        self.buttons: ButtonsBoard = []
        for i in range(self.model.rows):
            row = Frame(self.board)
            row.pack()
            self.buttons.append([])
            for j in range(self.model.columns):
                btn = Button(
                    row,
                    width=4, height=1,
                    font=('Corbel', 20),
                    command=lambda r=i, c=j: self.controller.on_left_click(r, c)
                )
                btn.bind(
                    '<Button-3>',
                    lambda event, r=i, c=j: self.controller.on_right_click(r, c)
                )
                btn.pack(side=LEFT)
                self.buttons[i].append(btn)
    
    def create_panel(self) -> None:
        panel = Frame(self)
        panel.pack(side=BOTTOM, fill=X)
        
        Button(
            panel,
            text='Новая игра',
            font=('Corbel', 16),
            command=self.controller.restart_game
        ).pack(side=RIGHT)
        
        Spinbox(
            panel,
            from_=MIN_MINES,
            to=MAX_MINES,
            textvariable=self.mines,
            width=4,
            font=('Corbel', 16),
        ).pack(side=RIGHT)
        Label(
            panel,
            text='Количество мин: ',
            font=('Corbel', 16)
        ).pack(side=RIGHT)
        
        Spinbox(
            panel,
            from_=MIN_COLUMNS,
            to=MAX_COLUMNS,
            textvariable=self.columns,
            width=3,
            font=('Corbel', 16)
        ).pack(side=RIGHT)
        Label(
            panel,
            text=' x ',
            font=('Corbel', 16)
        ).pack(side=RIGHT)
        
        Spinbox(
            panel,
            from_=MIN_ROWS,
            to=MAX_ROWS,
            textvariable=self.rows,
            width=3,
            font=('Corbel', 16)
        ).pack(side=RIGHT)
        Label(
            panel,
            text='Размер поля: ',
            font=('Corbel', 16)
        ).pack(side=RIGHT)
    
    @property
    def game_settings(self) -> tuple[int, int, int]:
        return int(self.rows.get()), int(self.columns.get()), int(self.mines.get())
    
    @staticmethod
    def show_win_message() -> None:
        showinfo('Поздравляем!', 'Вы победили!')
    
    @staticmethod
    def show_game_over_message() -> None:
        showinfo('Игра окончена', 'Вы проиграли')
    
    def sync_model(self) -> None:
        for i in range(self.model.rows):
            for j in range(self.model.columns):
                cell = self.model.get_cell(i, j)
                if cell is None:
                    return
                
                btn = self.buttons[i][j]
                
                if self.model.is_game_over() and cell.mined:
                    btn.config(bg='black', text='')
                
                if cell.state is States.CLOSED:
                    btn.config(text=States.CLOSED.value)
                elif cell.state is States.FLAGGED:
                    btn.config(text=States.FLAGGED.value)
                elif cell.state is States.QUESTIONED:
                    btn.config(text=States.QUESTIONED.value)
                elif cell.state is States.OPENED:
                    btn.config(relief=SUNKEN, text='')
                    if cell.counter > 0:
                        btn.config(text=cell.counter)
                    elif cell.mined:
                        btn.config(bg='red')
    
    def block_button(self, row: int, column: int, block: bool = True):
        btn = self.buttons[row][column]
        if not btn:
            return
        
        if block:
            btn.bind('<Button-1>', 'break')
        else:
            btn.unbind('<Button-1>')


class Game:
    def __init__(self, model_obj: Matrix):
        self.model = model_obj
        self.view: GUI = None
    
    def set_view(self, view_obj: GUI) -> None:
        self.view = view_obj
    
    def restart_game(self) -> None:
        self.model.create_matrix(*self.view.game_settings)
        self.view.create_board()
    
    def on_left_click(self, row: int, column: int) -> None:
        self.model.open_cell(row, column)
        self.view.sync_model()
        if self.model.is_win():
            self.view.show_win_message()
            self.restart_game()
        elif self.model.is_game_over():
            self.view.show_game_over_message()
            self.restart_game()
    
    def on_right_click(self, row: int, column: int) -> None:
        self.model.cell_cycle_state(row, column)
        self.view.sync_model()
        cell = self.model.matrix[row][column]
        self.view.block_button(
            row, column,
            cell.state is States.FLAGGED
        )


def main():
    """Точка входа."""
    m = Matrix()
    c = Game(m)
    
    root = Tk()
    root.title('Сапёр')
    v = GUI(m, c, root)
    
    v.pack()
    v.mainloop()


if __name__ == '__main__':
    main()
