from tkinter import *
from tkinter import ttk
from PIL import Image


def make_a_splash():
    splash_root = Tk()
    splash_root.title("Hello Splash")
    splash_root.geometry("300x200")
    splash_root.config(bg="#93ccfa")

    splash_label = ttk.Label(splash_root, text='Thanks for giving my app a try!', background="#93ccfa")
    splash_label.pack()




    return splash_root


