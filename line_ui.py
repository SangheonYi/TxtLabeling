from asyncio.windows_events import NULL
import tkinter as tk
from constants import ORIGIN, TOKENIZED, LABEL

def label_click(event,txt_labeling):
    print(event.widget)
    name = str(event.widget)
    index = int(name.split('-')[-1])
    current_token = event.widget['text'].split()[0]
    txt_labeling.files[TOKENIZED].set_label(index, txt_labeling.picked_label)
    event.widget['text'] = current_token + ' ' + txt_labeling.picked_label
    event.widget['bg'] = 'green'
    print(f'label clicked: {event}')

def init_label(txt_labeling, key):
    txt_labeling.labels[key] = [tk.Label(txt_labeling.app, textvariable=txt_labeling.texts[key])]
    txt_labeling.labels[key][0].grid(row=0, column=0)

# def label_file_label(txt_labeling):
#     txt_labeling.labels[LABEL] =


def update_label(txt_labeling, key):
    label_list = []
    mixed = []
    if txt_labeling.files[key] != NULL:
        text = f'{txt_labeling.files[key].current}th: {txt_labeling.files[key].get_line()}'
        mixed = txt_labeling.files[key].get_mixed_list()
        print(f'mixed: {mixed}')
        print(f'updated: {text}')
        txt_labeling.texts[key].set(text)
    for label in txt_labeling.labels[key]:
        label.destroy()
    print(key, txt_labeling.files[key])
    for i, token in enumerate(mixed):
        row = 0
        if key == TOKENIZED:
            row = 1
        label = tk.Label(txt_labeling.app, name=key + '-'+ str(i), text=token)
        label.grid(row=row, column=i)
        label.bind("<Button-1>", lambda event:label_click(event, txt_labeling))
        label_list.append(label)
    txt_labeling.labels[key] = label_list
    # txt_labeling.labels[key] = tk.Label(txt_labeling.app, textvariable=txt_labeling.texts[key]).grid()
    # txt_labeling.labels[key].pack()
