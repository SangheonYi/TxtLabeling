import random
import tkinter as tk
from constants import LABEL_DOMAIN_ROW, ORIGIN, TOKENIZED, LABEL
def rgb_to_hex(r, g, b):
    r, g, b = int(r), int(g), int(b)
    return '#' + hex(r)[2:].zfill(2) + hex(g)[2:].zfill(2) + hex(b)[2:].zfill(2)

def init_radio(txt_labeling):
    half_size = len(txt_labeling.files[LABEL].label_domain) // 4 - 1
    for i, label in enumerate(txt_labeling.files[LABEL].label_domain):
        radio_button = tk.Radiobutton(txt_labeling.app, text=label, value=label, variable=txt_labeling.picked_label)
        if not (label == 'O' or label == 'UNK'):
            red, green, blue = 240, 240, 120
            offset_base = 255 // half_size
            offset = i // 4
            if i % 4 > 1:
                green = offset * offset_base
                if label[-1] == 'I':
                    red -= 30
                    blue -= 30
                if green > 127:
                    red //= 2
            else:
                red = offset * offset_base
                blue = (half_size - offset) * offset_base
                if label[-1] == 'I':
                    green -= 30
            txt_labeling.color_dict[label] = rgb_to_hex(red, green, blue)
            radio_button.config(bg=txt_labeling.color_dict[label])
        radio_button.grid(row=LABEL_DOMAIN_ROW + (i // 10),column=i % 10)
        txt_labeling.label_domain.append(radio_button)
