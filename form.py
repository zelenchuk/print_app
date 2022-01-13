from tkinter import *
import tkinter as tk

# Import required libraries
from tkinter import *
from tkinter import ttk

fields = 'Last Name', 'First Name', 'Job', 'Country'


def fetch(entries):
    for entry in entries:
        field = entry[0]
        text = entry[1].get()
        print('%s: "%s"' % (field, text))


def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries


def enter_form(win):
    wdw = Toplevel(win)
    wdw.geometry('+400+400')

    ents = makeform(wdw, fields)
    win.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b1 = tk.Button(wdw, text='Show', command=(lambda e=ents: fetch(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(wdw, text='Quit', command=win.quit)
    b2.pack(side=tk.LEFT, padx=5, pady=5)

    return win.wait_window(wdw)


# Create an instance of tkinter frame
win = Tk()

# Set the window size
# win.resizable(False, False)  # This code helps to disable windows from resizing
win.attributes('-fullscreen', True)

window_height = 600
window_width = 1000

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))

win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
style = ttk.Style()
style.theme_use('clam')


# Define a function to implement choice function
def choice(win, label, option):
    if option == "yes":
        label.config(text="Hello, How are You?")
    else:
        label.config(text="You have selected No")
        win.wm_attributes("-disabled", False)


def click_fun(win):
    # global pop

    win.wm_attributes("-disabled", True)

    pop = Toplevel(win)
    pop.title("Confirmation")

    window_width = 400
    window_height = 250

    screen_width = pop.winfo_screenwidth()
    screen_height = pop.winfo_screenheight()

    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))

    pop.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    pop.config(bg="white")
    # Create a Label Text
    label = Label(pop, text="Would You like to Proceed?",
                  font=('Aerial', 12))
    label.pack(pady=20)
    # Add a Frame
    frame = Frame(pop, bg="gray71")
    frame.pack(pady=10)
    # Add Button for making selection
    button1 = Button(frame, text="Yes", command=lambda: choice(win, label, "yes"), bg="blue", fg="white")
    button1.grid(row=0, column=1)
    button2 = Button(frame, text="No", command=lambda: choice(win, label, "no"), bg="blue", fg="white")
    button2.grid(row=0, column=2)


    return win.wait_window(frame)


# Create a Label widget
label = Label(win, text="", font=('Aerial', 14))
label.pack(pady=40)

# Create a Tkinter button
ttk.Button(win, text="Форма", command=lambda: click_fun(win)).pack()

ttk.Button(win, text="Начать испытание", command=lambda: enter_form(win)).pack()

ttk.Button(win, text="О программе", command=lambda: win.destroy()).pack(pady=50)
ttk.Button(win, text="Закрыть программу", command=lambda: win.destroy()).pack()

win.mainloop()
