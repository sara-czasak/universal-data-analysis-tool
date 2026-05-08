from tkinter import ttk
from tkinter import *
from helpers import *


def create_button(operation, root, lang_center, analysis_brain, cols_selected):
    button = ttk.Button(root, text=lang_center.translate(operation), command=lambda: show_stat(button_id=operation, context={
        'analysis_brain': analysis_brain,
        'cols_selected': cols_selected,
        'lang_center': lang_center,
        'root': root,
        'button': button,
        }))
    return button


def reset_button_text(button, text, analysis_brain):
    if button.cget('text') == text:
        button.config(text='HIDE')
        if analysis_brain.stats_canvas is not None:
            analysis_brain.stats_canvas = None
    else:
        button.config(text=text)



# 'get_lowest_value', 'unique_values'
def show_stat(button_id, context):
    analysis_brain = context['analysis_brain']
    cols_selected = context['cols_selected'][0]
    lang_center = context['lang_center']
    root = context['root']
    button = context['button']

    if analysis_brain.stats_canvas is not None:
        analysis_brain.stats_canvas = None

    stats_canvas = Canvas(root)
    stats_canvas.grid(column=0, row=3, padx=10, pady=10)
    analysis_brain.stats_canvas = stats_canvas


    if button_id == 'get_highest_value':

        reset_button_text(button, f'{lang_center.translate("get_highest_value")}', analysis_brain)

        if analysis_brain.stats_canvas is not None:
            children = analysis_brain.stats_canvas.winfo_children()
            for child in children:
                if isinstance(child, ttk.Label):
                    child.destroy()

        highest = analysis_brain.get_highest_value(cols_selected)
        label = ttk.Label(stats_canvas, text=f'{lang_center.translate("The highest value in column ")} {cols_selected}: {highest}')
        label.grid(column=0, row=0)


    elif button_id == 'get_lowest_value':
        reset_button_text(button, f'{lang_center.translate("get_lowest_value")}', analysis_brain)

        if analysis_brain.stats_canvas is not None:
            children = analysis_brain.stats_canvas.winfo_children()
            for child in children:
                if isinstance(child, ttk.Label):
                    child.destroy()
            lowest = analysis_brain.get_lowest_value(cols_selected)
            label = ttk.Label(stats_canvas, text=f"{lang_center.translate('The lowest value in column ')} {cols_selected}: {lowest}")
            label.grid(column=0, row=0)


    elif button_id == 'unique_values':
        reset_button_text(button, f'{lang_center.translate("unique_values")}', analysis_brain)

        children = analysis_brain.stats_canvas.winfo_children()
        for child in children:
            if isinstance(child, ttk.Label):
                child.destroy()

        unique = analysis_brain.unique_values(cols_selected)
        if unique:
            len_unique = len(unique)
            if len_unique <= 100:
                cols = 4
            else:
                cols = 8
            col_count = 0
            row_count = 0
            for index, (value, count) in enumerate(unique.items()):
                label = ttk.Label(stats_canvas, text=f'{value}: {count}')
                if index % cols == 0 and index != 0:
                    label.grid(column=col_count, row=row_count)
                    col_count = 0
                    row_count += 1
                else:
                    label.grid(column=col_count, row=row_count)
                    col_count += 1
        button.config(text="HIDE")



