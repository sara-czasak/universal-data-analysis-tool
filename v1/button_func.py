from tkinter import ttk
from tkinter import *


def load_file_show_filename(context):
    lang_center = context['lang_center']
    analysis_brain = context['analysis_brain']
    filename_label = context['filename_label']
    get_file_button = context['get_file_button']
    listbox = context['listbox']

    analysis_brain.get_file()
    filename = analysis_brain.filename
    if filename_label.cget('text') == '':
        filename_label.config(text=f'{lang_center.translate("File name:")} {filename}')

    else:
        filename_label.config(text=f'{lang_center.translate("File name:")} {filename}')
    get_file_button.config(text=f'{lang_center.translate("CHANGE FILE")}')
    col_names = analysis_brain.columns
    if listbox.size() > 0:
        listbox.delete(0, END)
    if len(col_names) > 0:
        for i in col_names:
            listbox.insert(END, i)
            listbox.grid(column=0, row=1, columnspan=3, padx=10, pady=10)