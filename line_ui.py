from asyncio.windows_events import NULL
import tkinter as tk

from constants import ORIGIN, TOKENIZED

def init_label(txt_labeling, key):
    txt_labeling.lines[key] = [tk.Label(txt_labeling.app, textvariable=txt_labeling.texts[key])]
    txt_labeling.lines[key][0].grid(row=0, column=0)

def update_label(txt_labeling, key):
    label_list = []
    mixed = []
    if txt_labeling.files[key] != NULL:
        text = f'{txt_labeling.files[key].current}th: {txt_labeling.files[key].get_line()}'
        mixed = txt_labeling.files[key].get_mixed_list()
        print(f'mixed: {mixed}')
        print(f'updated: {text}')
        txt_labeling.texts[key].set(text)
    for label in txt_labeling.lines[key]:
        label.destroy()
    print(key, txt_labeling.files[key])
    for i, token in enumerate(mixed):
        row = 0
        if key == TOKENIZED:
            row = 1
        label = tk.Label(txt_labeling.app, text=token)
        label.grid(row=row, column=i)
        label_list.append(label)
    txt_labeling.lines[key] = label_list
    # txt_labeling.lines[key] = tk.Label(txt_labeling.app, textvariable=txt_labeling.texts[key]).grid()
    # txt_labeling.lines[key].pack()
