import asyncio
import threading

from tkinter import messagebox, Entry
import tkinter as tk
import tkinter.font as font
import tkinter.scrolledtext as scrolledtext


async def start_timer(label_filename, txt_edit):
    """ функция которая выполниться асинхронно в отдельном процессе """

    txt_edit.focus_set()

    for i in range(0, 10):
        label_filename.config(text=i, font=("Calibri", 44))
        # print("Hello World!" + str(i))
        await asyncio.sleep(1.0)

    result_text = txt_edit.get(1.0, tk.END)

    print("You typed: ", result_text)
    print("Symbols: ", len(result_text))

    txt_edit.delete(1.0, tk.END)  # Очищаю тект txt_edit
    label_filename.config(text='')  # Очищаю тект метки, после того как время выйдет

    messagebox.showinfo(message='Время вышло! Ты молодец!')
    messagebox.showinfo(message='Ты напечатал {} знаков за 120 секунд'.format(len(result_text.replace(" ", "")) - 1))


def _asyncio_thread(async_loop, label_filename, txt_edit):
    """ Асинхронный поток """
    async_loop.run_until_complete(start_timer(label_filename, txt_edit))


def do_tasks(async_loop, label_filename, txt_edit):
    """ Button-Event-Handler starting the asyncio part. """
    threading.Thread(target=_asyncio_thread, args=(async_loop, label_filename, txt_edit)).start()


def save_current_file(event=False):
    messagebox.showinfo(message='Файл сохранен (фейк)')


def start():
    elapsed_time = time.time() - start_var


def run_by_hot_key(async_loop, label_filename, txt_edit, event=None):
    return do_tasks(async_loop, label_filename, txt_edit)


def main(async_loop):
    window = tk.Tk()

    window.title("StarTyping - Конкурс по скорости печати")
    window.geometry("750x450")
    window.rowconfigure(0, minsize=500, weight=1)
    window.columnconfigure(1, minsize=500, weight=1)

    # implementing scrollbar functionality
    scrollbar = tk.Scrollbar(window)

    txt_edit = scrolledtext.ScrolledText(window, undo=True)  # add scrolledtext and ctrl + Z functionality
    fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)

    btn_do_tasks = tk.Button(fr_buttons, text="Начать", command=lambda: do_tasks(async_loop, label_filename, txt_edit))

    # Создаем метки
    label_filename = tk.Label(fr_buttons, text='')

    # Прикручиваем эти кнопки к дизайну
    btn_do_tasks.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

    # Настраиваем отображение основных елементов
    label_filename.grid(row=7, column=0, sticky="nsew", padx=5, pady=40)
    fr_buttons.grid(row=0, column=0, sticky="ns")
    txt_edit.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

    # define font
    myFont = font.Font(family='Helvetica', size=25)
    txt_edit['font'] = myFont  # установил шрифт и размеры для текстового поля

    # Создаем слушаетель комбинации клавиш для старта процесса.
    # передаю локальные переменные интерфейса, включая параметр event от метода .bind()
    window.bind('<Control-s>', lambda event: run_by_hot_key(async_loop, label_filename, txt_edit))

    # entry = Entry(window, width=30)
    # entry.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

    window.mainloop()


if __name__ == '__main__':
    async_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(async_loop)
    main(async_loop)
