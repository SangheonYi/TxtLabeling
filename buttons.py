from tkinter import Button
from constants import ORIGIN, TOKENIZED
import line_ui

def file_next(event, txt_labeling, key):
        print(f"버튼이 클릭되었습니다 {event}")
        file = txt_labeling.files[key]
        if file:
            file.next()
            print(file.current)
        line_ui.update_label(txt_labeling, key)

def file_prev(event, txt_labeling, key):
        print(f"버튼이 클릭되었습니다 {event}")
        file = txt_labeling.files[key]
        if file:
            file.prev()
            print(file.current)
        line_ui.update_label(txt_labeling, key)

def files_next(event, txt_labeling):
    file_next(event, txt_labeling, ORIGIN)
    file_next(event, txt_labeling, TOKENIZED)

def files_prev(event, txt_labeling):
    file_prev(event, txt_labeling, ORIGIN)
    file_prev(event, txt_labeling, TOKENIZED)

def button_init(txt_labeling):
    app = txt_labeling.app

    # Origin Next
    next_button = Button(app, text='Next')
    next_button.grid(row=3, column=0)
    next_button.bind('<Button-1>', lambda event: file_next(event, txt_labeling, ORIGIN))
    app.bind('<Right>', lambda event: files_next(event, txt_labeling))
    # Origin Previous
    prev_button = Button(app, text='Previous')
    prev_button.grid(row=3, column=1)
    prev_button.bind('<Button-1>', lambda event: file_prev(event, txt_labeling, ORIGIN))
    app.bind('<Left>', lambda event: files_prev(event, txt_labeling))

    # Tokenized Next
    next_button = Button(app, text='Tokenized Next')
    next_button.grid(row=3, column=2)
    next_button.bind('<Button-1>', lambda event: file_next(event, txt_labeling, TOKENIZED))
    app.bind('<Right>', lambda event: files_next(event, txt_labeling))
    # Tokenized Previous
    prev_button = Button(app, text='Tokenized Previous')
    prev_button.grid(row=3, column=3)
    prev_button.bind('<Button-1>', lambda event: file_prev(event, txt_labeling, TOKENIZED))
    app.bind('<Left>', lambda event: files_prev(event, txt_labeling))
