# https://www.studytonight.com/tkinter/text-editor-application-using-tkinter


import time

from tkinter import messagebox
import tkinter as tk
import tkinter.font as font

import tkinter.scrolledtext as scrolledtext

from core import save_file, open_file


start_var = time.time()

import asyncio
import threading


# моя функция которая выполниться асинхронно в отдельном процессе
async def hello_world(label_filename, txt_edit):
	for i in range(0, 121):
		label_filename.config(text=i, font=("Calibri", 44))
		# print("Hello World!" + str(i))
		await asyncio.sleep(1.0)
	messagebox.showinfo(message='Job is DONE!')
	result_text = txt_edit.get(1.0, tk.END)
	print("You typed: ", result_text)
	print("Symbols: ", len(result_text))
	txt_edit.delete(1.0, tk.END)


def _asyncio_thread(async_loop, label_filename, txt_edit):
	async_loop.run_until_complete(hello_world(label_filename, txt_edit))


def do_tasks(async_loop, label_filename, txt_edit):
	""" Button-Event-Handler starting the asyncio part. """
	threading.Thread(target=_asyncio_thread, args=(async_loop, label_filename, txt_edit)).start()


def do_freezed(event=False):
	message = 'Просто модальное окно для уведомлений'
	if event:
		message = 'Left pressed!'
	messagebox.showinfo(message=message)


def save_current_file(event=False):
	messagebox.showinfo(message='Файл сохранен (фейк)')


def start():
	elapsed_time = time.time() - start_var

	# print("elapsed time:", elapsed_time * 1000, "milliseconds")



def main(async_loop):
	window = tk.Tk()

	window.title("Текстовый редактор")
	window.rowconfigure(0, minsize=500, weight=1)
	window.columnconfigure(1, minsize=500, weight=1)


	# implementing scrollbar functionality
	scrollbar = tk.Scrollbar(window)

	
	txt_edit = scrolledtext.ScrolledText(window, undo=True)  # add scrolledtext and ctrl + Z functionality
	fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)

	# Создаем кнопки
	# btn_open = tk.Button(fr_buttons, text="Открыть документ", command=lambda:open_file(window, txt_edit))
	# btn_save = tk.Button(fr_buttons, text="Сохранить как ...", command=lambda:save_file(window, txt_edit))
	# btn_start = tk.Button(fr_buttons, text="Начать", command=start)
	btn_do_tasks = tk.Button(fr_buttons, text="Начать", command=lambda:do_tasks(async_loop, label_filename, txt_edit))
	# btn_freezed = tk.Button(fr_buttons, text='Freezed???', command=do_freezed)
	
	# Создаем метки
	label_filename = tk.Label(fr_buttons, text='')

	# Прикручиваем эти кнопки к дизайну
	# btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
	# btn_save.grid(row=1, column=0, sticky="ew", padx=5)
	# btn_start.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
	btn_do_tasks.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
	# btn_freezed.grid(row=6, column=0, sticky="ew", padx=5, pady=5)
	

	# Настраиваем отображение основных елементов
	label_filename.grid(row=7, column=0, sticky="nsew", padx=5, pady=40)
	fr_buttons.grid(row=0, column=0, sticky="ns")
	txt_edit.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)


	# define font
	myFont = font.Font(family='Helvetica', size=25)
	txt_edit['font'] = myFont  # установил шрифт и размеры для текстового поля

	
	# hotkey to save current file
	# window.bind('<Control-s>', save_current_file)
	window.mainloop()


if __name__ == '__main__':
	async_loop = asyncio.new_event_loop()
	asyncio.set_event_loop(async_loop)
	main(async_loop)
