from tkinter import Listbox, MULTIPLE, END
from constants import LABEL

def listbox_selected(event, txt_labeling, key):
    selection = event.widget.curselection()
    txt_labeling.label_listbox[key] = [event.widget.get(i) for i in selection]

def init_listbox(txt_labeling, key, column):
    label_listbox = Listbox(txt_labeling.app,selectmode=MULTIPLE,exportselection=0)
    for label in txt_labeling.files[LABEL].label_domain:
        label_listbox.insert(END, label)
    label_listbox.grid(row=20,column=column)
    label_listbox.bind("<<ListboxSelect>>", lambda event:listbox_selected(event, txt_labeling, key))
    return label_listbox