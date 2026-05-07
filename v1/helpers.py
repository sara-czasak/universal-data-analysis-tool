


def clean_up(root, *remove):
    children = root.winfo_children()
    for child in children:
        if child not in remove:
            child.grid_remove()