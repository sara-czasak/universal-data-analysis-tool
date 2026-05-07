from tkinter import ttk
from tkinter import *
import pandastable as pt
from helpers import *
from analysis_buttons import *
from helpers import *


def load_file_show_filename(context):
    lang_center = context['lang_center']
    analysis_brain = context['analysis_brain']
    filename_label = context['filename_label']
    get_file_button = context['get_file_button']
    listbox = context['listbox']
    head_button = context['head_button']
    select_cols_button = context['select_cols_button']

    analysis_brain.get_file()
    filename = analysis_brain.filename
    if filename_label.cget('text') == '':
        filename_label.config(text=f'{lang_center.translate("File name:")} {filename}')
    else:
        filename_label.config(text=f'{lang_center.translate("File name:")} {filename}')
    head_button.grid(column=0, row=1, padx=10, pady=10)
    select_cols_button.grid(column=1, row=1, padx=10, pady=10)
    get_file_button.config(text=f'{lang_center.translate("CHANGE FILE")}')
    col_names = analysis_brain.columns
    if listbox.size() > 0:
        listbox.delete(0, END)
    if len(col_names) > 0:
        for i in col_names:
            listbox.insert(END, i)


def show_col_names(listbox, analysis_brain, head_button, lang_center, select_cols_button, get_cols_button):
    if analysis_brain.tree is not None:
        analysis_brain.tree.destroy()
        analysis_brain.tree = None
        head_button.config(text=lang_center.translate('SHOW FIRST 5 ROWS'))
    if not listbox.winfo_viewable():
        listbox.grid(column=1, row=2, columnspan=3, padx=10, pady=10)
        select_cols_button.config(text=lang_center.translate('HIDE COLUMNS'))
        get_cols_button.grid(column=0, row=2, padx=10, pady=10)
    else:
        listbox.grid_remove()
        select_cols_button.config(text=lang_center.translate('SELECT COLUMNS'))
        get_cols_button.grid_remove()


def show_df_head(context):
    root = context['root']
    analysis_brain = context['analysis_brain']
    head_button = context['head_button']
    lang_center = context['lang_center']
    listbox = context['listbox']
    select_cols_button = context['select_cols_button']

    if listbox.winfo_viewable():
        listbox.grid_remove()
        select_cols_button.config(text=lang_center.translate('SELECT COLUMNS'))

    if analysis_brain.tree and analysis_brain.tree.winfo_exists():
        analysis_brain.tree.destroy()
        analysis_brain.tree = None
        head_button.config(text=lang_center.translate('SHOW FIRST 5 ROWS'))

    else:
        col_names = analysis_brain.columns.tolist()
        # view head
        analysis_brain.tree = ttk.Treeview(root, show='headings', columns=col_names)
        for col in col_names:
            if len(col_names) >= 10:
                analysis_brain.tree.heading(col, text=col)
                analysis_brain.tree.column(col, width=60)
            else:
                analysis_brain.tree.heading(col, text=col)
                analysis_brain.tree.column(col, width=100)
            analysis_brain.tree.grid(column=1, row=2, columnspan=3, padx=10, pady=10)
            head_button.config(text=lang_center.translate('HIDE ROWS'))


def get_selected_cols(context):
    listbox = context['listbox']
    analysis_brain = context['analysis_brain']
    select_cols_button = context['select_cols_button']
    lang_center = context['lang_center']
    get_cols_button = context['get_cols_button']
    root = context['root']

    if listbox.winfo_viewable():
        listbox.grid_remove()
        select_cols_button.config(text=lang_center.translate('SELECT COLUMNS'))
    cols_selected = []
    for i in listbox.curselection():
        cols_selected.append(listbox.get(i))
        get_cols_button.grid_remove()
    operations = analysis_brain.get_available_operations(cols_selected)
    buttons = [create_button(operation, root, lang_center, analysis_brain, cols_selected) for operation in operations]
    for index, button in enumerate(buttons):
        button.grid(column=index, row=2, padx=10, pady=10)

