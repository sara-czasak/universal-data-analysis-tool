from tkinter import ttk
from tkinter import *

from pandas.core.sample import process_sampling_size

from popups import *


# TODO 1: Make get_selected_columns_advanced return a list of selected columns and print to console else return None and feedback for user (Please select at least 2 columns)


def select_columns_advanced(context):
    multiple_column_selection_advanced = context['multiple_column_selection_advanced']
    select_columns_advanced_btn = context['select_columns_advanced_btn']
    lang_center = context['lang_center']
    get_selected_columns_advanced_btn = context['get_selected_columns_advanced_btn']
    analysis_brain = context['analysis_brain']
    advanced_stats_buttons_frame = context['advanced_stats_buttons_frame']
    advanced_stats_frame = context['advanced_stats_frame']


    index = multiple_column_selection_advanced.curselection()
    if len(index) > 0:
        index = index[0]
        item = multiple_column_selection_advanced.get(index)
        # Do this only if an item wasn't selected yet
        if analysis_brain.col_set_type is None:
            if analysis_brain.data_types_in_cols[item] != 'str':
                analysis_brain.col_set_type = 'num'
                analysis_brain.column_selection_advanced.append(item)
                initial_col_selected = analysis_brain.column_selection_advanced
                populate_list({
                    'redraw': True,
                    'analysis_brain': analysis_brain,
                    'multiple_column_selection_advanced': multiple_column_selection_advanced,
                    'get_selected_columns_advanced_btn': get_selected_columns_advanced_btn,
                    'select_columns_advanced_btn': select_columns_advanced_btn,
                    'lang_center': lang_center,
                    'type_data': analysis_brain.col_set_type,
                    'initial_col_selected': initial_col_selected,
                    'advanced_stats_buttons_frame': advanced_stats_buttons_frame,
                    'advanced_stats_frame': advanced_stats_frame,
                })
            else:
                analysis_brain.col_set_type = 'str'
                analysis_brain.column_selection_advanced.append(item)
                initial_col_selected = analysis_brain.column_selection_advanced
                populate_list({
                    'redraw': True,
                    'analysis_brain': analysis_brain,
                    'multiple_column_selection_advanced': multiple_column_selection_advanced,
                    'get_selected_columns_advanced_btn': get_selected_columns_advanced_btn,
                    'select_columns_advanced_btn': select_columns_advanced_btn,
                    'lang_center': lang_center,
                    'type_data': analysis_brain.col_set_type,
                    'initial_col_selected': initial_col_selected,
                    'advanced_stats_buttons_frame': advanced_stats_buttons_frame,
                    'advanced_stats_frame': advanced_stats_frame,
                })


        # elif analysis_brain.col_set_type == 'num':
        #     initial_col_selected = analysis_brain.column_selection_advanced
        #     populate_list({
        #         'redraw': True,
        #         'analysis_brain': analysis_brain,
        #         'multiple_column_selection_advanced': multiple_column_selection_advanced,
        #         'get_selected_columns_advanced_btn': get_selected_columns_advanced_btn,
        #         'select_columns_advanced_btn': select_columns_advanced_btn,
        #         'lang_center': lang_center,
        #         'type_data': analysis_brain.col_set_type,
        #         'initial_col_selected': initial_col_selected,
        #         'advanced_stats_buttons_frame': advanced_stats_buttons_frame,
        #     })
        #
        #
        # elif analysis_brain.col_set_type == 'str':
        #     initial_col_selected = analysis_brain.column_selection_advanced
        #     populate_list({
        #         'redraw': True,
        #         'analysis_brain': analysis_brain,
        #         'multiple_column_selection_advanced': multiple_column_selection_advanced,
        #         'get_selected_columns_advanced_btn': get_selected_columns_advanced_btn,
        #         'select_columns_advanced_btn': select_columns_advanced_btn,
        #         'lang_center': lang_center,
        #         'type_data': analysis_brain.col_set_type,
        #         'initial_col_selected': initial_col_selected,
        #         'advanced_stats_buttons_frame': advanced_stats_buttons_frame,
        #     })


def get_selected_columns_advanced(context):
    multiple_column_selection_advanced = context['multiple_column_selection_advanced']
    select_columns_advanced_btn = context['select_columns_advanced_btn']
    lang_center = context['lang_center']
    get_selected_columns_advanced_btn = context['get_selected_columns_advanced_btn']
    analysis_brain = context['analysis_brain']
    advanced_stats_buttons_frame = context['advanced_stats_buttons_frame']

    # TODO 1: Make a filtering mechanism so only values that can have an operation done on them can be selected. E.g.: select one column -> empty listbox -> redraw listbox with selected col at the top and only columns that can have an operation done on them below.


    multiple_column_selection_advanced.grid_remove()
    select_columns_advanced_btn.config(text=lang_center.translate('SELECT COLUMNS'))
    get_selected_columns_advanced_btn.grid_remove()


def populate_list(context, redraw=False):
    analysis_brain = context['analysis_brain']
    advanced_stats_frame = context['advanced_stats_frame']
    advanced_stats_buttons_frame = context['advanced_stats_buttons_frame']
    multiple_column_selection_advanced =  context['multiple_column_selection_advanced']
    get_selected_columns_advanced_btn = context['get_selected_columns_advanced_btn']
    select_columns_advanced_btn = context['select_columns_advanced_btn']
    lang_center = context['lang_center']



    if analysis_brain.columns is not None:

        if len(analysis_brain.column_selection_advanced) > 0:
            initial_col_selected = context['initial_col_selected']

            # TODO find all columns that match the dtype.

            items = initial_col_selected
            if analysis_brain.col_set_type == 'num':
                for i in analysis_brain.data_types_in_cols:
                    if analysis_brain.data_types_in_cols[i] != 'str' and i not in items:
                        items.append(i)
            elif analysis_brain.col_set_type == 'str':
                for i in analysis_brain.data_types_in_cols:
                    if analysis_brain.data_types_in_cols[i] == 'str' and i not in items:
                        items.append(i)

            print(items)

            multiple_column_selection_advanced.delete(0, END)
            if items is not None:
                for item in items:
                    multiple_column_selection_advanced.insert(END, item)

                    multiple_column_selection_advanced.selection_set(0)
                    multiple_column_selection_advanced.config(selectmode=MULTIPLE)

                multiple_column_selection_advanced.grid(column=1, row=2, columnspan=3, padx=10, pady=10)
                get_selected_columns_advanced_btn.grid(column=0, row=2, padx=10, pady=10)
                get_selected_columns_advanced_btn.config(command=lambda: get_selected_columns_advanced({
                    'multiple_column_selection_advanced': multiple_column_selection_advanced,
                    'select_columns_advanced_btn': select_columns_advanced_btn,
                    'lang_center': lang_center,
                    'get_selected_columns_advanced_btn': get_selected_columns_advanced_btn,
                    'analysis_brain': analysis_brain,
                    'advanced_stats_buttons_frame': advanced_stats_buttons_frame,
                    'advanced_stats_frame': advanced_stats_frame,
                }))
                select_columns_advanced_btn.config(text=lang_center.translate('HIDE COLUMNS'))
        else:


            items = analysis_brain.columns

            multiple_column_selection_advanced.delete(0, END)

            for item in items:
                multiple_column_selection_advanced.insert(END, item)

            multiple_column_selection_advanced.grid(column=1, row=2, columnspan=3, padx=10, pady=10)
            get_selected_columns_advanced_btn.grid(column=0, row=2, padx=10, pady=10)
            get_selected_columns_advanced_btn.config(command=lambda: get_selected_columns_advanced({
                'multiple_column_selection_advanced': multiple_column_selection_advanced,
                'select_columns_advanced_btn': select_columns_advanced_btn,
                'lang_center': lang_center,
                'get_selected_columns_advanced_btn': get_selected_columns_advanced_btn,
                'analysis_brain': analysis_brain,
                'advanced_stats_buttons_frame': advanced_stats_buttons_frame,
                'advanced_stats_frame': advanced_stats_frame,
            }))
            select_columns_advanced_btn.config(text=lang_center.translate('HIDE COLUMNS'))
            multiple_column_selection_advanced.bind('<<ListboxSelect>>', lambda event: select_columns_advanced({
                'multiple_column_selection_advanced': multiple_column_selection_advanced,
                'select_columns_advanced_btn': select_columns_advanced_btn,
                'lang_center': lang_center,
                'get_selected_columns_advanced_btn': get_selected_columns_advanced_btn,
                'analysis_brain': analysis_brain,
                'advanced_stats_buttons_frame': advanced_stats_buttons_frame,
                'advanced_stats_frame': advanced_stats_frame,
            }))
    else:
        return





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
    multiple_column_selection_advanced = context["multiple_column_selection_advanced"]


    if analysis_brain.tree and analysis_brain.tree.winfo_exists():
        analysis_brain.tree.destroy()
        analysis_brain.tree = None


    if button_id == 'advanced':
        get_selected_columns_advanced_btn = context["get_selected_columns_advanced_btn"]

        stats_frame.grid_remove()
        stats_buttons_frame.grid_remove()

        for i in stats_frame.winfo_children():
            i.grid_remove()
        for i in stats_buttons_frame.winfo_children():
            i.grid_remove()

        advanced_stats_buttons_frame.grid(column=1, row=1)
        advanced_stats_frame.grid(column=1, row=2)
        advanced_or_basic_label.config(text=lang_center.translate('Advanced Analysis'))


        # UI BUILD
        select_columns_advanced_btn.grid(column=1, row=0, padx=10, pady=10)
        select_columns_advanced_btn.config(text=lang_center.translate('SELECT COLUMNS'), command=lambda: [
            setattr(analysis_brain, 'column_selection_advanced', []),
            setattr(analysis_brain, 'col_set_type', None),
            populate_list({
                'analysis_brain': analysis_brain,
                'advanced_stats_frame': advanced_stats_frame,
                'multiple_column_selection_advanced': multiple_column_selection_advanced,
                'get_selected_columns_advanced_btn': get_selected_columns_advanced_btn,
                'select_columns_advanced_btn': select_columns_advanced_btn,
                'lang_center': lang_center,
                'advanced_stats_buttons_frame': advanced_stats_buttons_frame,
            })
        ])
        # select_columns_advanced_btn.config(text=lang_center.translate('SELECT COLUMNS'), command=lambda: populate_list({
        #     'analysis_brain': analysis_brain,
        #     'advanced_stats_frame': advanced_stats_frame,
        #     'multiple_column_selection_advanced': multiple_column_selection_advanced,
        #     'get_selected_columns_advanced_btn': get_selected_columns_advanced_btn,
        #     'select_columns_advanced_btn': select_columns_advanced_btn,
        #     'lang_center': lang_center,
        #     'advanced_stats_buttons_frame': advanced_stats_buttons_frame,
        # }))


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

