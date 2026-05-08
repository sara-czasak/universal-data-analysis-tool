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

    # tree = ttk.Treeview(frm, columns=['job_name', 'job_type', 'public_transport', 'job_address', 'date_applied', 'job_status'], show='tree headings', height=10)
    # tree.heading('job_name', text='Job Name')
    # tree.column('job_name', width=100)
    # tree.heading('job_type', text='Job Type')
    # tree.column('job_type', width=100)
    # tree.heading('public_transport', text='Public Transport')
    # tree.column('public_transport', width=100)
    # tree.heading('job_address', text='Job Address')
    # tree.column('job_address', width=100)
    # tree.heading('date_applied', text='Date Applied')
    # tree.column('date_applied', width=100)
    # tree.heading('job_status', text='Job Status')
    # tree.column('job_status', width=100)
    # for cat in categories:
    #     parent_id = tree.insert('', 'end', text=cat)
    #     for _, row in data[cat].iterrows():
    #         tree.insert(parent_id, 'end', values=list(row.values))
    # return tree