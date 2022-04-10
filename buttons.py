from tkinter import Button
from constants import ORIGIN
import line_ui

def file_next(event, app, txt_labeling, key):
        print(f"버튼이 클릭되었습니다 {event}")
        file = txt_labeling.files[key]
        if file:
            file.next()
            print(file.current)
        line_ui.update_label(app, txt_labeling, key)

def files_next(event, app, txt_labeling):
    file_next(event, app, txt_labeling, ORIGIN)

def button_init(app, txt_labeling):
    next_button = Button(app, text='Next')
    next_button.pack()
    next_button.bind('<Button-1>', lambda event: file_next(event, app, txt_labeling, ORIGIN))
    app.bind('<Right>', lambda event: files_next(event, app, txt_labeling))
