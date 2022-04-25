import tkinter as tk
from Listbox import init_listbox
from constants import LABEL_BUTTON_ROW, LABEL
def rgb_to_hex(r, g, b):
    r, g, b = int(r), int(g), int(b)
    return '#' + hex(r)[2:].zfill(2) + hex(g)[2:].zfill(2) + hex(b)[2:].zfill(2)

def init_radio(txt_labeling):
    for button in txt_labeling.label_buttons:
        button.destroy()
    color_equlize_size = len(txt_labeling.files[LABEL].label_domain) // 6
    if color_equlize_size == 0:
        color_equlize_size = 1
    for i, label in enumerate(txt_labeling.files[LABEL].label_domain):
        radio_button = tk.Radiobutton(txt_labeling.app, text=label, value=label, variable=txt_labeling.picked_label)
        if not (label == 'O' or label == 'UNK'):
            red, green, blue = 214, 214, 214
            offset_base = 255 // color_equlize_size
            offset = i // 6
            i_mod = i % 6
            color_salt = 75
            
            if  i_mod < 2:
                red = offset * offset_base
                green = color_salt
            elif 1 < i_mod < 4:
                green = offset * offset_base
                blue = color_salt
            else:
                red = color_salt
                blue = offset * offset_base
            if label[-1] == 'I':
                red = red // 2 + 30
                green = green // 2 + 30
                blue = blue // 2 + 30
            txt_labeling.color_dict[label] = rgb_to_hex(red, green, blue)
            radio_button.config(bg=txt_labeling.color_dict[label])
        radio_button.grid(row=LABEL_BUTTON_ROW + (i // 10),column=i % 10)
        txt_labeling.label_buttons.append(radio_button)
    init_listbox(txt_labeling)
