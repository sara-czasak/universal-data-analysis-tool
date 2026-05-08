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
            tree.insert(parent_id, 'end', values=list(row))

    return tree
