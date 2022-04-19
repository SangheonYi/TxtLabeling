from asyncio.windows_events import NULL
from constants import *
import tkinter as tk

class TXTLabeling():
    def __init__(self, app) -> None:
        self.app = app
        self.picked_label = tk.StringVar()

        # index to explore
        self.current_progress = tk.StringVar()
        self.entry_index = tk.StringVar()

        # label filter
        self.selected_label_listbox = []

        # opend files
        self.files = {
            ORIGIN : NULL,
            TOKENIZED : NULL,
            LABEL : NULL,
        }
        self.label_domain = []
        self.color_dict = {}

        # Label UI list
        self.labels = {
            INDEX : NULL,
            ORIGIN : [],
            TOKENIZED : [],
        }