from tkinter import ttk
from tkinter import *
from helpers import *
from stats_trees import *


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
        return True
    else:
        button.config(text=text)
        return False


def show_stat(button_id, context):
    print(f"show_stat called: {button_id}")

    analysis_brain = context['analysis_brain']
    cols_selected = context['cols_selected'][0]
    lang_center = context['lang_center']
    root = context['root']
    button = context['button']


    if button_id == 'get_highest_value':
        if not reset_button_text(button, f'{lang_center.translate("get_highest_value")}', analysis_brain):
            if analysis_brain.stats_canvas is not None:
                analysis_brain.stats_canvas.destroy()
                analysis_brain.stats_canvas = None
        else:
            stats_canvas = Canvas(root)
            stats_canvas.grid(column=0, row=3, padx=10, pady=10)
            analysis_brain.stats_canvas = stats_canvas



            highest = analysis_brain.get_highest_value(cols_selected)
            label = ttk.Label(stats_canvas, text=f'{lang_center.translate("The highest value in column ")} {cols_selected}: {highest}')
            label.grid(column=0, row=0)


    elif button_id == 'get_lowest_value':
        if not reset_button_text(button, f'{lang_center.translate("get_lowest_value")}', analysis_brain):
            if analysis_brain.stats_canvas is not None:
                analysis_brain.stats_canvas.destroy()
                analysis_brain.stats_canvas = None
        else:

            stats_canvas = Canvas(root)
            stats_canvas.grid(column=0, row=3, padx=10, pady=10)
            analysis_brain.stats_canvas = stats_canvas
            print(analysis_brain.stats_canvas)
            print(id(stats_canvas))

            lowest = analysis_brain.get_lowest_value(cols_selected)
            label = ttk.Label(stats_canvas, text=f"{lang_center.translate('The lowest value in column ')} {cols_selected}: {lowest}")
            label.grid(column=0, row=0)


    elif button_id == 'unique_values':
        if not reset_button_text(button, f'{lang_center.translate("unique_values")}', analysis_brain):
            if analysis_brain.stats_canvas is not None:
                analysis_brain.stats_canvas.destroy()
                analysis_brain.stats_canvas = None
        else:

            stats_canvas = Canvas(root)
            stats_canvas.grid(column=0, row=3, padx=10, pady=10)
            analysis_brain.stats_canvas = stats_canvas

            unique = analysis_brain.unique_values(cols_selected)

            if unique:
                values = [i for i in unique.keys()]
                all_rows = []
                for value in values:
                    rows = analysis_brain.get_rows(cols_selected, value)
                    all_rows.append(rows)

                print('cols selected: ', cols_selected)
                tree = grow_tree(canvas=stats_canvas, context={
                    'categories': unique,
                    'column_names': analysis_brain.columns,
                    'cols_selected': cols_selected,
                    'rows': all_rows,
                })
                tree.grid(column=0, row=0, columnspan=4, padx=10, pady=10)
