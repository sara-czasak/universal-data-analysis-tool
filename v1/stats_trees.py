import tkinter as tk
from tkinter import ttk



def grow_tree(canvas, context):
    categories = context['categories']
    col_names = context['column_names']
    cols_selected = context['cols_selected']
    all_rows = context['rows']

    print("COLUMNS:", col_names)

    tree = ttk.Treeview(canvas, columns=col_names, show='tree headings', height=10)

    for name in col_names:
        tree.heading(name, text=name)
        tree.column(name, width=50)

    for i, parent_name in enumerate(categories.keys()):
        parent_id = tree.insert("", 'end', text=parent_name)

        rows = all_rows[i]

        for _, row in rows.iterrows():
            values = ['' if str(v).lower() == 'nan' else v for v in row]
            tree.insert(parent_id, 'end', values=values)

    return tree


def advanced_tree_grow(frm, context):
    columns = context['columns']
    new_df = context['new_df']
    button = context['button']

    tree = ttk.Treeview(frm, columns=columns, show='headings', height=5)

    for column in columns:
        tree.heading(column, text=column)
        tree.column(column, width=60)

    for _, row in new_df.iterrows():
        tree.insert('', 'end', values=list(row))

    tree.grid(column=0, row=0, padx=10, pady=10, columnspan=3)


