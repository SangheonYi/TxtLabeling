import tkinter as tk
from tkinter import filedialog
import File
from functools import partial
from constants import *

def open_datafile(files, key):
    file_path = filedialog.askopenfilename(initialdir = ".",title = "Open file",filetypes = (("tsv file","*.tsv"),("All files","*.*")))
    print(file_path)
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            files[key] = File.DataTSV(file)
            print(files[key].get_line(0))

def open_labelfile(files, key):
    file_path = filedialog.askopenfilename(initialdir = ".",title = "Open file",filetypes = (("label file","*.txt"),("All files","*.*")))
    print(file_path)
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            files[key] = File.LabelFile(file)
            print(files[key].get_label(0))

def onSave():
    print(filedialog.asksaveasfilename(initialdir = ".",title = "Save as",filetypes = (("tsv file","*.tsv"),("All files","*.*"))))

def menu_init(app, files):
    menubar = tk.Menu(app, tearoff=0)

    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label=OPEN_ORIGIN_FILE, command=partial(open_datafile, files=files, key=ORIGIN))
    filemenu.add_command(label=OPEN_TOKEN_FILE, command=partial(open_datafile, files=files, key=TOKENIZED))
    filemenu.add_command(label=OPEN_LABEL_FILE, command=partial(open_labelfile, files=files, key=LABEL))
    filemenu.add_command(label="Save", command=onSave)
    filemenu.add_command(label="Exit", command=app.quit)

    menubar.add_cascade(label="File", menu=filemenu)

    app.config(menu=menubar)
