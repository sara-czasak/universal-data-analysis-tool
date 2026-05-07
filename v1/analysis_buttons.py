from tkinter import ttk
from tkinter import *
from language_center import *
from helpers import *


def create_button(operation, root, lang_center):
    print(f'Making button: {operation}')
    button = ttk.Button(root, text=lang_center.translate(operation), command=lambda: show_stat(button_id=operation))
    return button


def show_stat(button_id):
    pass