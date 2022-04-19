from asyncio.windows_events import NULL
from constants import *
import tkinter as tk

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