import tkinter as tk
from tkinter import filedialog
import File
from constants import *
import line_ui
import label_domain_radio

def open_datafile(event, txt_labeling, key):
    file_path = filedialog.askopenfilename(initialdir = ".",title = "Open file",filetypes = (("tsv file","*.tsv"),("All files","*.*")))
    if file_path:
        with open(file_path, "r", encoding="utf-8") as data_file:
            txt_labeling.files[key] = File.DataTSV(data_file)
        line_ui.update_label(txt_labeling, key)

def open_labelfile(event, txt_labeling):
    file_path = filedialog.askopenfilename(initialdir = ".",title = "Open file",filetypes = (("label file","*.txt"),("All files","*.*")))
    if file_path:
        with open(file_path, "r", encoding="utf-8") as label_file:
            txt_labeling.files[LABEL] = File.LabelFile(label_file)
        label_domain_radio.init_radio(txt_labeling)

def on_save(event, txt_labeling):
    file_path = filedialog.asksaveasfilename(initialdir = ".",title = "Save as",filetypes = (("tsv file","*.tsv"),("All files","*.*")))
    if file_path:
        with open(file_path + '.tsv', "w", encoding="utf-8") as save_file:
            edited_file = txt_labeling.files[TOKENIZED]
            for i, e in enumerate(edited_file.tokens_list):
                save_file.write(edited_file.get_ith_line(i) + '\n')


def menu_init(txt_labeling):
    menubar = tk.Menu(txt_labeling.app, tearoff=0)

    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label=OPEN_ORIGIN_FILE, command=lambda event=OPEN_ORIGIN_FILE: open_datafile(event, txt_labeling, key=ORIGIN))
    filemenu.add_command(label=OPEN_TOKEN_FILE, command=lambda event=OPEN_TOKEN_FILE: open_datafile(event, txt_labeling, key=TOKENIZED))
    filemenu.add_command(label=OPEN_LABEL_FILE, command=lambda event=OPEN_LABEL_FILE: open_labelfile(event, txt_labeling))
    filemenu.add_command(label="Save", command=lambda event="Save": on_save(event, txt_labeling))
    filemenu.add_command(label="Exit", command=txt_labeling.app.quit)

    menubar.add_cascade(label="File", menu=filemenu)

    txt_labeling.app.config(menu=menubar)
