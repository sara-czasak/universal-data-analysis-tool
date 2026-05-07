from tkinter import ttk
from tkinter import *
from language_center import *
from analysis_brain import *


root = Tk()
root.title('Universal Data Analyser')


lang_center = LanguageCenter()
analysis_brain = AnalysisBrain()


def load_file_show_filename():
    analysis_brain.get_file()
    filename = analysis_brain.filename
    if filename_label.cget('text') == '':
        filename_label.config(text=f'{lang_center.translate("File name:")} {filename}')
    else:
        filename_label.config(text=f'{lang_center.translate("File name:")} {filename}')
    get_file_button.config(text=f'{lang_center.translate("CHANGE FILE")}')


get_file_button = ttk.Button(root, text=lang_center.translate('LOAD FILE'), command=load_file_show_filename)
get_file_button.grid(column=3, row=0, padx=10, pady=10)

filename_label = ttk.Label(root, text='')
filename_label.grid(column=0, row=0, columnspan=3, padx=10, pady=10)






root.mainloop()