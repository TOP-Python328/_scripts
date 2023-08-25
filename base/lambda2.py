from tkinter import Tk, Button

root = Tk()
root.title('Тестовое GUI приложение')
root.geometry('400x300')


def change_title(new_title: str) -> None:
    root.title(new_title)


Button(
    root,
    text='ПЕРВЫЙ ЗАГОЛОВОК',
    # анонимная функция используется в качестве обёртки, которая позволяет записать вызов другой функции с аргументами
    command=lambda: change_title('Новый Заголовок Окна'),
).grid(
    row=0, column=0, 
    sticky='nsew', 
    padx=100, pady=50
)
Button(
    root,
    text='ВТОРОЙ ЗАГОЛОВОК',
    # анонимная функция используется в качестве обёртки, которая позволяет записать вызов другой функции с аргументами
    command=lambda: change_title('Ещё Один Заголовок Окна'),
).grid(
    row=1, column=0, 
    sticky='nsew', 
    padx=100, pady=50
)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)

root.mainloop()
