from tkinter import ttk
from tkinter import *
from language_center import *
from helpers import *


def create_button(operation, root, lang_center, analysis_brain, cols_selected):
    print(f'Making button: {operation}')
    button = ttk.Button(root, text=lang_center.translate(operation), command=lambda: show_stat(button_id=operation, context={
        'analysis_brain': analysis_brain,
        'cols_selected': cols_selected,
        }))
    return button


# 'get_lowest_value', 'unique_values'
def show_stat(button_id, context):
    analysis_brain = context['analysis_brain']
    cols_selected = context['cols_selected'][0]

    if button_id == 'get_highest_value':
        highest = analysis_brain.get_highest_value(cols_selected)
        print(f"The highest value in column: {cols_selected} is {highest}")

    elif button_id == 'get_lowest_value':
        lowest = analysis_brain.get_lowest_value(cols_selected)
        print(f"The lowest value in column: {cols_selected} is {lowest}")

    elif button_id == 'unique_values':
        unique = analysis_brain.unique_values(cols_selected)
        print("UNIQUE")
        for item in unique:
            print(item)