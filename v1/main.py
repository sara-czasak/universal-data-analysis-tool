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
}))
get_file_button.grid(column=3, row=0, padx=10, pady=10)

filename_label = ttk.Label(root, text='')
filename_label.grid(column=0, row=0, columnspan=3, padx=10, pady=10)


# Column list
listbox = Listbox(root, height=10, selectmode=MULTIPLE)




root.mainloop()