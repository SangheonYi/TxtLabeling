from tkinter import Entry
from constants import ORIGIN, TOKENIZED
import buttons 
def init_entry(txt_labeling):
    line_index_entry = Entry(txt_labeling.app, width=8, textvariable=txt_labeling.entry_index)
    line_index_entry.grid(row=101)

def update_idx(event, txt_labeling):
    input_idx = txt_labeling.entry_index.get()
    if input_idx.isnumeric():
        input_idx = int(input_idx) + 1
        if txt_labeling.files[ORIGIN]:
            txt_labeling.files[ORIGIN].go_ith_line(input_idx)
        if txt_labeling.files[TOKENIZED]:
            txt_labeling.files[TOKENIZED].go_ith_line(input_idx)
        buttons.files_prev(event, txt_labeling)