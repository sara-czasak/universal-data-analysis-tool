from tkinter import ttk
from tkinter import *
from language_center import *
from analysis_brain import *
from button_func import *
from style_mgr import *


root = Tk()
root.title('Universal Data Analyser')
root.minsize(1000, 400)

bg = tk.PhotoImage(file = "./img/plastic-texture-holographic-background.png")

root.columnconfigure(0, minsize=0, weight=1)
root.columnconfigure(1, minsize=100)
root.columnconfigure(2, minsize=0, weight=1)

my_style = StyleWidgets(root)

bg_label = Label(root, image=bg)
bg_label.place(x=0, y=0)

home_frame = ttk.Frame(root)
home_frame.grid(column=1, row=0)
root.columnconfigure(0, minsize=0, weight=1)

home_frame.columnconfigure(0, minsize=0, weight=1)
home_frame.columnconfigure(1, minsize=0)

stats_buttons_frame = ttk.Frame(root)
stats_buttons_frame.grid(column=1, row=1)

stats_buttons_frame.columnconfigure(0, minsize=0)
stats_buttons_frame.columnconfigure(1, minsize=0)
stats_buttons_frame.columnconfigure(2, minsize=0)


stats_frame = ttk.Frame(root)
stats_frame.grid(column=1, row=2)

stats_frame.columnconfigure(0, minsize=0)
stats_frame.columnconfigure(1, minsize=0)
stats_frame.columnconfigure(2, minsize=0)

bg_main_frame = Label(home_frame, image=bg)
bg_main_frame.place(x=0, y=0)
bg_stats_frame = Label(stats_frame, image=bg)
bg_stats_frame.place(x=0, y=0)
bg_stats_button_frame = Label(stats_buttons_frame, image=bg)
bg_stats_button_frame.place(x=0, y=0)

lang_center = LanguageCenter()
analysis_brain = AnalysisBrain(lang_center)

filename_label = ttk.Label(home_frame, text='')
filename_label.grid(column=1, row=0, padx=10, pady=10)

get_file_button = ttk.Button(home_frame, text=lang_center.translate('LOAD FILE'), command=lambda: load_file_show_filename({
    'analysis_brain': analysis_brain,
    'lang_center': lang_center,
    'get_file_button': get_file_button,
    'filename_label': filename_label,
    'listbox': listbox,
    'head_button': head_button,
    'select_cols_button': select_cols_button,
    'home_frame': home_frame,
    'stats_buttons_frame': stats_buttons_frame,
}))
get_file_button.grid(column=0, row=0, padx=10, pady=10)



# Show df head
head_button = ttk.Button(stats_buttons_frame, text=lang_center.translate('SHOW TABLE'), command=lambda: show_df_head({
    'analysis_brain': analysis_brain,
    'stats_frame': stats_frame,
    'listbox': listbox,
    'head_button': head_button,
    'lang_center': lang_center,
    'select_cols_button': select_cols_button,
    'get_cols_button': get_cols_button,
    'stats_buttons_frame': stats_buttons_frame,
}))


# Show col names
select_cols_button = ttk.Button(stats_buttons_frame, text=lang_center.translate('SELECT COLUMN'), command=lambda: show_col_names(listbox, analysis_brain, head_button, lang_center, select_cols_button, get_cols_button, stats_buttons_frame, stats_frame))

# Column list
listbox = Listbox(stats_buttons_frame, height=10, selectmode=SINGLE)

get_cols_button = ttk.Button(stats_buttons_frame, text=lang_center.translate('OK'), command=lambda: get_selected_cols({
    'listbox': listbox,
    'analysis_brain': analysis_brain,
    'lang_center': lang_center,
    'select_cols_button': select_cols_button,
    'get_cols_button': get_cols_button,
    'stats_buttons_frame': stats_buttons_frame,
    'stats_frame': stats_frame,
    'home_frame': home_frame,
    'img': bg,
}))
root.mainloop()