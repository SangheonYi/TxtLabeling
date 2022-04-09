import tkinter as tk

def label_init(app):
    origin_line = tk.Label(app, text='Hello origin_line')
    tokenized_line = tk.Label(app, text='Hello tokenized_line')
    origin_line.pack()
    tokenized_line.pack()
