import tkinter as tk
from Listbox import init_listbox
from constants import LABEL_DOMAIN_ROW, ORIGIN, TOKENIZED, LABEL
def rgb_to_hex(r, g, b):
    r, g, b = int(r), int(g), int(b)
    return '#' + hex(r)[2:].zfill(2) + hex(g)[2:].zfill(2) + hex(b)[2:].zfill(2)

def init_radio(txt_labeling):
    half_size = len(txt_labeling.files[LABEL].label_domain) // 6
    for i, label in enumerate(txt_labeling.files[LABEL].label_domain):
        radio_button = tk.Radiobutton(txt_labeling.app, text=label, value=label, variable=txt_labeling.picked_label)
        if not (label == 'O' or label == 'UNK'):
            red, green, blue = 255, 255, 255
            offset_base = 255 // half_size
            offset = i // 6
            i_mod = i % 6
            
            if  i_mod < 2:
                red = offset * offset_base
                green = 0
            elif 1 < i_mod < 4:
                green = offset * offset_base
                blue = 0
            else:
                red = 0
                blue = offset * offset_base
            if label[-1] == 'I':
                red = red // 2 + 30
                green = green // 2 + 30
                blue = blue // 2 + 30
            txt_labeling.color_dict[label] = rgb_to_hex(red, green, blue)
            radio_button.config(bg=txt_labeling.color_dict[label])
        radio_button.grid(row=LABEL_DOMAIN_ROW + (i // 10),column=i % 10)
        txt_labeling.label_domain.append(radio_button)
    init_listbox(txt_labeling)
