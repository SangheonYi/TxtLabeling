import tkinter as tk
from constants import ORIGIN, TOKENIZED

def init_label(app, txt_labeling, key):
    txt_labeling.lines[key] = tk.Label(app, textvariable=txt_labeling.texts[key])
    txt_labeling.lines[key].pack()

def update_label(app, txt_labeling, key):
    if txt_labeling.files[key]:
        text = txt_labeling.files[key].get_line()
        print(f'updated: {text}')
        txt_labeling.texts[key].set(text)

def update_labels(app, txt_labeling):
    update_label(app, txt_labeling, ORIGIN)
