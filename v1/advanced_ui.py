from tkinter import ttk
from tkinter import *


# TODO 1: PLACE RELEVANT BUTTONS ON ADVANCED UI
# TODO 2: REMOVE RELEVANT BUTTONS ON BASIC UI



def swap_frames(button_id, context):
    stats_frame = context['stats_frame']
    stats_buttons_frame = context['stats_buttons_frame']
    advanced_stats_frame = context['advanced_stats_frame']
    advanced_stats_buttons_frame = context['advanced_stats_buttons_frame']
    advanced_analysis_button = context['advanced_analysis_button']
    basic_analysis_button = context['basic_analysis_button']
    advanced_or_basic_label = context['advanced_or_basic_label']
    lang_center = context['lang_center']
    analysis_brain = context['analysis_brain']
    head_button = context['head_button']
    select_columns_advanced_btn = context["select_columns_advanced_btn"]
    select_cols_button = context["select_cols_button"]

    if analysis_brain.tree and analysis_brain.tree.winfo_exists():
        analysis_brain.tree.destroy()
        analysis_brain.tree = None


    if button_id == 'advanced':
        stats_frame.grid_remove()
        stats_buttons_frame.grid_remove()

        for i in stats_frame.winfo_children():
            i.grid_remove()
        for i in stats_buttons_frame.winfo_children():
            i.grid_remove()

        advanced_stats_buttons_frame.grid(column=1, row=1)
        advanced_stats_frame.grid(column=1, row=2)
        advanced_or_basic_label.config(text=lang_center.translate('Advanced Analysis'))

        select_columns_advanced_btn.grid(column=1, row=0, padx=10, pady=10)
        select_columns_advanced_btn.config(text=lang_center.translate('SELECT COLUMNS'))

        basic_analysis_button.grid(column=3, row=0, padx=10, pady=10)
        advanced_analysis_button.grid_remove()

    elif button_id == 'basic':
        advanced_stats_frame.grid_remove()
        advanced_analysis_button.grid_remove()
        advanced_stats_buttons_frame.grid_remove()

        for i in advanced_stats_frame.winfo_children():
            i.grid_remove()
        for i in advanced_stats_buttons_frame.winfo_children():
            i.grid_remove()

        head_button.grid(column=1, row=0, padx=10, pady=10)
        head_button.config(text=lang_center.translate('SHOW TABLE'))
        select_cols_button.grid(column=2, row=0, padx=10, pady=10)
        select_cols_button.config(text=lang_center.translate('SELECT COLUMN'))

        stats_frame.grid(column=1, row=2)
        stats_buttons_frame.grid(column=1, row=1)

        advanced_or_basic_label.config(text=lang_center.translate('Basic Analysis'))

        advanced_analysis_button.grid(column=3, row=0, padx=10, pady=10)

        basic_analysis_button.grid_remove()

