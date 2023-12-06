"""
View (MVC): графическое представление.
"""

from collections.abc import Iterable
from time import sleep
from tkinter import Tk, Frame, StringVar, Label, Button, Entry, Text

import controller


root = Tk()
root.title('Демонстратор MVC')
root.geometry('670x670-100+10')

mainframe = Frame(root, padx=10, pady=10)
mainframe.grid(row=0, column=0, sticky='nsew')

top_lbl_text = StringVar()
Label(
    mainframe,
    textvariable=top_lbl_text,
    font=('Franklin Gothic', 22)
).grid(row=0, column=0, sticky='new')

Button(
    mainframe,
    text='Показать всех людей',
    font=('Franklin Gothic Cond', 18),
    command=controller.get_all_people
).grid(row=1, column=0, sticky='new', pady=20)

entry_langs = StringVar()
Entry(
    mainframe,
    textvariable=entry_langs,
    font=('Fira Mono', 20)
).grid(row=2, column=0, sticky='new', pady=(20, 5), ipady=5)

Button(
    mainframe,
    text='Показать людей, владеющих языком',
    font=('Franklin Gothic Cond', 18),
    command=lambda: controller.get_people_by_lang(entry_langs.get())
).grid(row=3, column=0, sticky='new', pady=(0, 20))

btm_text = Text(
    mainframe,
    font=('Franklin Gothic', 16),
    padx=5, pady=5
)
btm_text.grid(row=4, column=0, sticky='nsew')

Button(
    mainframe,
    text='Выход',
    font=('Franklin Gothic Cond', 18),
    command=controller.end
).grid(row=5, column=0, sticky='new', pady=(20, 0))

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.columnconfigure(0, weight=1)


def greeting() -> None:
    top_lbl_text.set('Приветствую в демонстраторе MVC!')
    root.mainloop()


def people(data: Iterable[str]) -> None:
    btm_text.delete('1.0', 'end')
    btm_text.insert('1.0', '\n'.join(data))
    root.update_idletasks()


def bye() -> None:
    top_lbl_text.set('Пока!')
    root.update_idletasks()
    sleep(1.5)
    root.quit()

