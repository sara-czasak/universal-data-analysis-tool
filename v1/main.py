from tkinter import ttk
from tkinter import *
from language_center import *
from analysis_brain import *
from button_func import *


root = Tk()
root.title('Universal Data Analyser')


lang_center = LanguageCenter()
analysis_brain = AnalysisBrain()


get_file_button = ttk.Button(root, text=lang_center.translate('LOAD FILE'), command=lambda: load_file_show_filename({
    'analysis_brain': analysis_brain,
    'lang_center': lang_center,
    'get_file_button': get_file_button,
    'filename_label': filename_label,
    'listbox': listbox,
    'head_button': head_button,
    'select_cols_button': select_cols_button,
}))
get_file_button.grid(column=3, row=0, padx=10, pady=10)

filename_label = ttk.Label(root, text='')
filename_label.grid(column=0, row=0, columnspan=3, padx=10, pady=10)


# Show df head
head_button = ttk.Button(root, text=lang_center.translate('SHOW FIRST 5 ROWS'), command=lambda: show_df_head({
    'analysis_brain': analysis_brain,
    'root': root,
    'listbox': listbox,
    'head_button': head_button,
    'lang_center': lang_center,
    'select_cols_button': select_cols_button,
}))


# Show col names
select_cols_button = ttk.Button(root, text=lang_center.translate('SELECT COLUMNS'), command=lambda: show_col_names(listbox, analysis_brain, head_button, lang_center, select_cols_button, get_cols_button))

# Column list
listbox = Listbox(root, height=10, selectmode=MULTIPLE)

get_cols_button = ttk.Button(root, text=lang_center.translate('OK'), command=lambda: get_selected_cols({
    'listbox': listbox,
    'analysis_brain': analysis_brain,
    'lang_center': lang_center,
    'select_cols_button': select_cols_button,
    'get_cols_button': get_cols_button,
}))

root.mainloop()