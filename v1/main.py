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
    filename_label = Label(root, text=f'{lang_center.translate("File name:")} {filename}')
    filename_label.pack()



get_file_button = Button(root, text=lang_center.translate('Load File'), command=load_file_show_filename)
get_file_button.pack()








root.mainloop()