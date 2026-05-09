from tkinter import ttk
from tkinter import *
from helpers import *
from stats_trees import *


def create_button(operation, home_frame, lang_center, analysis_brain, cols_selected, stats_buttons_frame, stats_frame):
    button = ttk.Button(stats_frame, text=lang_center.translate(operation), command=lambda: show_stat(button_id=operation, context={
        'analysis_brain': analysis_brain,
        'cols_selected': cols_selected,
        'lang_center': lang_center,
        'home_frame': home_frame,
        'button': button,
        'stats_buttons_frame': stats_buttons_frame,
        'stats_frame': stats_frame,
        }))
    button.id = operation
    return button


def clean_ui(stats_frame):
    for child in stats_frame.winfo_children():
        if not isinstance(child, ttk.Button):
            child.destroy()


def reset_button_text(button, text, analysis_brain):
    all_btns = analysis_brain.operation_buttons
    if button.cget('text') != 'HIDE':
        button.config(text='HIDE')
        for btn in all_btns:
            if btn.id != button.id:
                btn.config(text=btn.id)
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
    stats_buttons_frame = context['stats_buttons_frame']

    stats_frame.grid(column=1, row=2)


    if button_id == 'get_highest_value':
        if reset_button_text(button, f'{lang_center.translate("get_highest_value")}', analysis_brain):
            for child in stats_buttons_frame.winfo_children():
                if isinstance(child, ttk.Button):
                    pass

            highest = analysis_brain.get_highest_value(cols_selected)
            label = ttk.Label(stats_frame, text=f'{lang_center.translate("The highest value in column ")} {cols_selected}: {highest}')

            row_index = (stats_frame.grid_size()[0]) + 1
            label.grid(column=0, row=row_index, columnspan=3)

        else:
            clean_ui(stats_frame)


    elif button_id == 'get_lowest_value':
        if reset_button_text(button, f'{lang_center.translate("get_lowest_value")}', analysis_brain):

            lowest = analysis_brain.get_lowest_value(cols_selected)
            label = ttk.Label(stats_frame, text=f"{lang_center.translate('The lowest value in column ')} {cols_selected}: {lowest}")

            row_index = (stats_frame.grid_size()[0]) + 1
            label.grid(column=0, row=row_index, columnspan=3)

        else:
            clean_ui(stats_frame)



    elif button_id == 'get_average':
        if reset_button_text(button, f'{lang_center.translate("get_average")}', analysis_brain):
            average = analysis_brain.get_average(cols_selected)
            label = ttk.Label(stats_frame, text=f'{lang_center.translate("The average value in column ")} {cols_selected}: {average:.2f}')

            row_index = (stats_frame.grid_size()[0]) + 1
            label.grid(column=0, row=row_index, columnspan=3)

        else:
            clean_ui(stats_frame)



    elif button_id == 'get_median':
        if reset_button_text(button, f'{lang_center.translate("get_median")}', analysis_brain):
            median = analysis_brain.get_median(cols_selected)
            label = ttk.Label(stats_frame, text=f'{lang_center.translate("The median value in column ")} {cols_selected}: {median:.2f}')

            row_index = (stats_frame.grid_size()[0]) + 1
            label.grid(column=0, row=row_index, columnspan=3)

        else:
            clean_ui(stats_frame)


    elif button_id == 'get_most_frequent':
        if reset_button_text(button, f'{lang_center.translate("get_most_frequent")}', analysis_brain):
            most_frequent = analysis_brain.get_most_frequent(cols_selected)
            label = ttk.Label(stats_frame, text=f'{lang_center.translate("The most frequent value in column ")} {cols_selected}: {most_frequent}')

            row_index = (stats_frame.grid_size()[0]) + 1
            label.grid(column=0, row=row_index, columnspan=3)

        else:
            clean_ui(stats_frame)


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
                row_index = (stats_frame.grid_size()[0]) + 1
                tree.grid(column=0, row=row_index, columnspan=10, padx=10, pady=10)

        else:
            clean_ui(stats_frame)
