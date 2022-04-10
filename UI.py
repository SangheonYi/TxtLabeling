from asyncio.windows_events import NULL
from msilib import sequence
import tkinter as tk
import line_ui
import menu
import buttons
from constants import *

class TXTLabeling():
    def __init__(self, app) -> None:
        self.app = app
        self.sequence = NULL
        self.files = {
            ORIGIN : NULL,
            TOKENIZED : NULL,
            LABEL : NULL,
        }
        self.lines = {
            ORIGIN : NULL,
            TOKENIZED : NULL,
        }
        self.texts = {
            ORIGIN : tk.StringVar(),
            TOKENIZED : tk.StringVar(),
        }
        self.texts[ORIGIN].set('Hello world')
        self.texts[TOKENIZED].set('Hello tokenized_line')

txt_labeling = TXTLabeling(tk.Tk())
app = txt_labeling.app
app.geometry('600x400')
app.title("Basic Menu Bar")

line_ui.update_labels(app, txt_labeling)
line_ui.init_label(app, txt_labeling, ORIGIN)
line_ui.init_label(app, txt_labeling, TOKENIZED)
buttons.button_init(app, txt_labeling)
menu.menu_init(app, txt_labeling.files)

app.mainloop()
