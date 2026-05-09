from tkinter import ttk
from tkinter import *
from language_center import *
from analysis_brain import *
from button_func import *


root = Tk()
root.title('Universal Data Analyser')
root.minsize(400, 400)

home_frame = ttk.Frame(root, padding=10)
home_frame.grid(column=0, row=0)

stats_buttons_frame = ttk.Frame(root, padding=10)
stats_buttons_frame.grid(column=0, row=1)

stats_frame = ttk.Frame(root, padding=10)
stats_frame.grid(column=0, row=2)


lang_center = LanguageCenter()
analysis_brain = AnalysisBrain()


get_file_button = ttk.Button(home_frame, text=lang_center.translate('LOAD FILE'), command=lambda: load_file_show_filename({
    'analysis_brain': analysis_brain,
    'lang_center': lang_center,
    'get_file_button': get_file_button,
    'filename_label': filename_label,
    'listbox': listbox,
    'head_button': head_button,
    'select_cols_button': select_cols_button,
    'home_frame': home_frame,
}))
get_file_button.grid(column=3, row=0, padx=10, pady=10)

filename_label = ttk.Label(home_frame, text='')
filename_label.grid(column=0, row=0, columnspan=2, padx=10, pady=10)


# Show df head
head_button = ttk.Button(stats_buttons_frame, text=lang_center.translate('SHOW TABLE'), command=lambda: show_df_head({
    'analysis_brain': analysis_brain,
    'home_frame': home_frame,
    'listbox': listbox,
    'head_button': head_button,
    'lang_center': lang_center,
    'select_cols_button': select_cols_button,
    'get_cols_button': get_cols_button,
}))


# Show col names
select_cols_button = ttk.Button(stats_buttons_frame, text=lang_center.translate('SELECT COLUMNS'), command=lambda: show_col_names(listbox, analysis_brain, head_button, lang_center, select_cols_button, get_cols_button, stats_buttons_frame))

# Column list
listbox = Listbox(home_frame, height=10, selectmode=SINGLE)

get_cols_button = ttk.Button(home_frame, text=lang_center.translate('OK'), command=lambda: get_selected_cols({
    'listbox': listbox,
    'analysis_brain': analysis_brain,
    'lang_center': lang_center,
    'select_cols_button': select_cols_button,
    'get_cols_button': get_cols_button,
    'stats_buttons_frame': stats_buttons_frame,
}))

root.mainloop()