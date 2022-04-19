import tkinter as tk
import menu
import buttons
import Entry
import TXTLabeling

txt_labeling = TXTLabeling(tk.Tk())
app = txt_labeling.app
app.geometry('600x400')
app.title("Basic Menu Bar")

buttons.button_init(txt_labeling)
menu.menu_init(txt_labeling)
Entry.init_entry(txt_labeling)

app.bind('<Return>', lambda event: Entry.update_idx(event, txt_labeling))
app.mainloop()
