from asyncio.windows_events import NULL
from msilib import sequence
import tkinter as tk
import menu
import buttons
import Entry
from constants import *

class TXTLabeling():
    def __init__(self, app) -> None:
        self.app = app
        self.sequence = NULL
        self.picked_label = tk.StringVar()
        self.current_progress = tk.StringVar()
        self.entry_index = tk.StringVar()
        self.label_domain = []
        self.color_dict = {}
        self.files = {
            ORIGIN : NULL,
            TOKENIZED : NULL,
            LABEL : NULL,
        }
        self.labels = {
            INDEX : NULL,
            ORIGIN : [],
            TOKENIZED : [],
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

buttons.button_init(txt_labeling)
menu.menu_init(txt_labeling)
Entry.init_entry(txt_labeling)

app.bind('<Return>', lambda event: Entry.update_idx(event, txt_labeling))
app.mainloop()
