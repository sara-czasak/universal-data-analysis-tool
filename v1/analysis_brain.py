# LOAD FILE AS DF
# ANALYSIS FUNCTIONS
# MAKE IT A CLASS
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk, filedialog


class AnalysisBrain:
    def __init__(self):
        self.filepath = None
        self.filename = None
        self.good_extensions = [{
            'excel': ['xls', 'xlsx', 'xlsm', 'xlsb', 'odf', 'ods', 'odt'],
            'csv': ['csv'],
        }]


    def get_file(self):
        self.filepath = filedialog.askopenfilename()
        self.filename = self.filepath.split('/')[-1]
        print(self.filename)
        self.create_dataframe()
        return self.filename


    def create_dataframe(self):
        file_extension = self.filename.split('.')[-1]
        for extension in self.good_extensions:
            if file_extension in extension['excel']:
                df = pd.read_excel(self.filepath)
                print(df.columns.values)
            elif file_extension in extension['csv']:
                df = pd.read_csv(self.filepath)
                print(df.columns.values)
            else:
                print('wrong file extension')

