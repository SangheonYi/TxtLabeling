from tkinter import Listbox, MULTIPLE, END
from constants import LABEL

def listbox_selected(event, txt_labeling):
    selection = event.widget.curselection()
    txt_labeling.selected_label_listbox = [event.widget.get(i) for i in selection]

def init_listbox(txt_labeling):
    label_listbox = Listbox(txt_labeling.app,selectmode=MULTIPLE,exportselection=0)
    for label in txt_labeling.files[LABEL].label_domain:
        label_listbox.insert(END, label)
    label_listbox.grid(row=20,column=0)
    label_listbox.bind("<<ListboxSelect>>", lambda event:listbox_selected(event, txt_labeling))
    return label_listbox