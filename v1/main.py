from tkinter import ttk
from tkinter import *
from language_center import *
from analysis_brain import *
from button_func import *
from style_mgr import *
from splash_screen import *
from advanced_ui import *
from report_writer import *


splash_root = make_a_splash()


def main():
    splash_root.destroy()
    root = Tk()
    root.title('Universal Data Analyser')
    root.minsize(1000, 500)

    root.columnconfigure(0, minsize=0, weight=1)
    root.columnconfigure(1, minsize=100)
    root.columnconfigure(2, minsize=0, weight=1)

    my_style = StyleWidgets(root)

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



    # FRAMES TO HANDLE ADVANCED ANALYSIS
    advanced_stats_buttons_frame = ttk.Frame(root)
    # advanced_stats_buttons_frame.grid(column=1, row=1)

    advanced_stats_frame = ttk.Frame(root)
    # advanced_stats_frame.grid(column=1, row=2)



    lang_center = LanguageCenter()
    analysis_brain = AnalysisBrain(lang_center)

    filename_label = ttk.Label(home_frame, text='')
    filename_label.grid(column=1, row=0, padx=10, pady=10)


    # Advanced UI elements !!!
    select_columns_advanced_btn = ttk.Button(advanced_stats_buttons_frame)
    multiple_column_selection_advanced = Listbox(advanced_stats_frame, selectmode=SINGLE)
    get_selected_columns_advanced_btn = ttk.Button(advanced_stats_frame, text='OK')


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
        'get_report_button' : get_report_button,
        'advanced_analysis_button': advanced_analysis_button,
        'advanced_or_basic_label': advanced_or_basic_label,
    }))
    get_file_button.grid(column=0, row=0, padx=10, pady=10)


    advanced_analysis_button = ttk.Button(home_frame, text=lang_center.translate('GO TO\nADVANCED\nANALYSIS'), command=lambda: swap_frames(button_id='advanced', context = {
        'stats_frame': stats_frame,
        'stats_buttons_frame': stats_buttons_frame,
        'advanced_stats_buttons_frame': advanced_stats_buttons_frame,
        'advanced_stats_frame': advanced_stats_frame,
        'advanced_analysis_button': advanced_analysis_button,
        'basic_analysis_button': basic_analysis_button,
        'advanced_or_basic_label': advanced_or_basic_label,
        'lang_center': lang_center,
        'analysis_brain': analysis_brain,
        'head_button': head_button,
        'select_columns_advanced_btn': select_columns_advanced_btn,
        'select_cols_button': select_cols_button,
        'multiple_column_selection_advanced': multiple_column_selection_advanced,
        'get_selected_columns_advanced_btn': get_selected_columns_advanced_btn,
    }))

    basic_analysis_button = ttk.Button(home_frame, text=lang_center.translate('GO TO\nBASIC\nANALYSIS'), command=lambda: swap_frames(button_id='basic', context = {
        'stats_frame': stats_frame,
        'stats_buttons_frame': stats_buttons_frame,
        'advanced_stats_buttons_frame': advanced_stats_buttons_frame,
        'advanced_stats_frame': advanced_stats_frame,
        'advanced_analysis_button': advanced_analysis_button,
        'basic_analysis_button': basic_analysis_button,
        'advanced_or_basic_label': advanced_or_basic_label,
        'lang_center': lang_center,
        'analysis_brain': analysis_brain,
        'head_button': head_button,
        'select_cols_button': select_cols_button,
        'select_columns_advanced_btn': select_columns_advanced_btn,
        'multiple_column_selection_advanced': multiple_column_selection_advanced,
    }))


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

    def save_report():
        report = ReportWriter(analysis_brain)


    get_report_button = ttk.Button(home_frame, text="SAVE REPORT", command=save_report)

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
    }))


    advanced_or_basic_label = ttk.Label(home_frame, text=lang_center.translate("Basic Analysis"))


splash_root.after(500, main)


mainloop()