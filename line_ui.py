import tkinter as tk

def init_label(txt_labeling, key):
    txt_labeling.lines[key] = tk.Label(txt_labeling.app, textvariable=txt_labeling.texts[key])
    txt_labeling.lines[key].pack()

def update_label(txt_labeling, key):
    if txt_labeling.files[key]:
        text = f'{txt_labeling.files[key].current}th: {txt_labeling.files[key].get_line()}'
        print(f'updated: {text}')
        txt_labeling.texts[key].set(text)
