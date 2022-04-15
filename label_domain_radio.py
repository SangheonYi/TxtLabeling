import random
import tkinter as tk
from constants import LABEL_DOMAIN_ROW, ORIGIN, TOKENIZED, LABEL
def rgb_to_hex(r, g, b):
    r, g, b = int(r), int(g), int(b)
    return '#' + hex(r)[2:].zfill(2) + hex(g)[2:].zfill(2) + hex(b)[2:].zfill(2)
    
def init_radio(txt_labeling):
    for i, label in enumerate(txt_labeling.files[LABEL].label_domain):
        radio_button = tk.Radiobutton(txt_labeling.app, text=label, value=label, variable=txt_labeling.picked_label)
        if not (label == 'O' or label == 'UNK'):
            txt_labeling.color_dict[label] = rgb_to_hex(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            radio_button.config(bg=txt_labeling.color_dict[label])
        radio_button.grid(row=LABEL_DOMAIN_ROW + (i // 10),column=i % 10)
        txt_labeling.label_domain.append(radio_button)
