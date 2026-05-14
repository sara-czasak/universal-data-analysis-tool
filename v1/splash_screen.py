from tkinter import *
from tkinter import ttk
from PIL import Image
from style_mgr import *


def make_a_splash(root):
    splash_root = Toplevel(root)
    splash_root.title("Hello Splash")
    splash_root.geometry("1000x500")
    splash_root.config(bg="#93ccfa")

    my_style = StyleWidgets(splash_root)

    splash_label = ttk.Label(splash_root, text='Thanks for giving my app a try!', background="#93ccfa")
    splash_label.pack()




    return splash_root


