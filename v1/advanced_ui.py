


def swap_frames(button_id, context):
    stats_frame = context['stats_frame']
    stats_buttons_frame = context['stats_buttons_frame']
    advanced_stats_frame = context['advanced_stats_frame']
    advanced_stats_buttons_frame = context['advanced_stats_buttons_frame']
    advanced_analysis_button = context['advanced_analysis_button']
    basic_analysis_button = context['basic_analysis_button']
    advanced_or_basic_label = context['advanced_or_basic_label']
    lang_center = context['lang_center']

    if button_id == 'advanced':
        stats_frame.grid_remove()
        stats_buttons_frame.grid_remove()
        advanced_stats_buttons_frame.grid(column=1, row=1)
        advanced_stats_frame.grid(column=1, row=2)
        advanced_or_basic_label.config(text=lang_center.translate('Advanced Analysis'))

        basic_analysis_button.grid(column=3, row=0, padx=10, pady=10)
        advanced_analysis_button.grid_remove()


    elif button_id == 'basic':
        advanced_stats_frame.grid_remove()
        advanced_analysis_button.grid_remove()
        stats_frame.grid(column=1, row=2)
        stats_buttons_frame.grid(column=1, row=1)
        advanced_or_basic_label.config(text=lang_center.translate('Basic Analysis'))

        advanced_analysis_button.grid(column=3, row=0, padx=10, pady=10)
        basic_analysis_button.grid_remove()

