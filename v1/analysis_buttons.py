from tkinter import ttk
from tkinter import *
from helpers import *
from stats_trees import *


def create_button(operation, home_frame, lang_center, analysis_brain, cols_selected, stats_frame):
    button = ttk.Button(home_frame, text=lang_center.translate(operation), command=lambda: show_stat(button_id=operation, context={
        'analysis_brain': analysis_brain,
        'cols_selected': cols_selected,
        'lang_center': lang_center,
        'home_frame': home_frame,
        'button': button,
        'stats_frame': stats_frame,
        }))
    return button


def reset_button_text(button, text, analysis_brain):
    if button.cget('text') == text:
        button.config(text='HIDE')
        return True
    else:
        button.config(text=text)
        return False


def show_stat(button_id, context):
    print(f"show_stat called: {button_id}")

    analysis_brain = context['analysis_brain']
    cols_selected = context['cols_selected'][0]
    lang_center = context['lang_center']
    home_frame = context['home_frame']
    button = context['button']
    stats_frame = context['stats_frame']

    children = stats_frame.winfo_children()
    for child in children:
        child.destroy()


    if button_id == 'get_highest_value':
        if reset_button_text(button, f'{lang_center.translate("get_highest_value")}', analysis_brain):

            highest = analysis_brain.get_highest_value(cols_selected)
            label = ttk.Label(stats_frame, text=f'{lang_center.translate("The highest value in column ")} {cols_selected}: {highest}')
            label.grid(column=0, row=0)


    elif button_id == 'get_lowest_value':
        if reset_button_text(button, f'{lang_center.translate("get_lowest_value")}', analysis_brain):

            lowest = analysis_brain.get_lowest_value(cols_selected)
            label = ttk.Label(stats_frame, text=f"{lang_center.translate('The lowest value in column ')} {cols_selected}: {lowest}")
            label.grid(column=0, row=0)


    elif button_id == 'unique_values':
        if reset_button_text(button, f'{lang_center.translate("unique_values")}', analysis_brain):

            unique = analysis_brain.unique_values(cols_selected)

            if unique:
                values = [i for i in unique.keys()]
                all_rows = []
                for value in values:
                    rows = analysis_brain.get_rows(cols_selected, value)
                    all_rows.append(rows)

                print('cols selected: ', cols_selected)
                tree = grow_tree(canvas=stats_frame, context={
                    'categories': unique,
                    'column_names': analysis_brain.columns,
                    'cols_selected': cols_selected,
                    'rows': all_rows,
                })
                tree.grid(column=0, row=0, columnspan=4, padx=10, pady=10)
