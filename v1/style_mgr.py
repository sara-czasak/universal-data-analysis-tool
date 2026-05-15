from tkinter import ttk, font



class StyleWidgets:
    def __init__(self, frm):
        self.frm = frm
        self.bg_color = "#93ccfa"
        self.my_theme()


    def my_theme(self):
        # self.frm.configure(bg=self.bg_color)
        style = ttk.Style()
        style.configure('TButton', font=('Verdana', 15))
        style.map('TButton', foreground=[('pressed', 'blue'), ('!pressed', 'black')],
                  background=[('pressed', 'blue'), ('!pressed', 'white')])
        style.configure('TLabel', font=('Verdana', 15))
        style.configure('Treeview', font=('Verdana', 8))

