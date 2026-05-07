


def clean_up(root, *exclude):
    children = root.winfo_children()
    for child in children:
        if child not in exclude:
            child.grid_remove()