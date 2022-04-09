from asyncio.windows_events import NULL
from msilib import sequence
import tkinter as tk
import line_ui
import menu
from constants import *

sequence = NULL

files = {
    ORIGIN : NULL,
    TOKENIZED : NULL,
    LABEL : NULL,
}

app = tk.Tk()
app.geometry('600x400')
app.title("Basic Menu Bar")

line_ui.label_init(app)
menu.menu_init(app, files)

app.mainloop()
