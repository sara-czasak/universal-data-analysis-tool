import tkinter as tk
from tkinter import messagebox


# Handle user error feedback
def feedback(message, lang_center):
    popup = tk.messagebox.showwarning(title=lang_center.translate("Error"), message=lang_center.translate(message))
    return popup