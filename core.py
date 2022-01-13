import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file(window, txt_edit, event=False):
	"""Open a file for editing."""
	filepath = askopenfilename(
		filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
	)

	if not filepath:
		return
	txt_edit.delete(1.0, tk.END)
	with open(filepath, "r") as input_file:
		text = input_file.read()
		txt_edit.insert(tk.END, text)
	window.title(f"Текстовый редактор - {filepath}")


def save_file(window, txt_edit, event=False):
	# print(txt_edit.get(1.0, tk.END))

	"""Save the current file as a new file."""
	filepath = asksaveasfilename(
		defaultextension="txt",
		filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
	)
	if not filepath:
		return
	with open(filepath, "w") as output_file:
		text = txt_edit.get(1.0, tk.END)
		output_file.write(text)
	window.title(f"Текстовый редактор - {filepath}")
