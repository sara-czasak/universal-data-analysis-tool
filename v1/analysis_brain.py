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
        self.columns = None
        self.df = None
        self.tree = None
        self.data_types_in_cols = {}
        self.good_extensions = [{
            'excel': ['xls', 'xlsx', 'xlsm', 'xlsb', 'odf', 'ods', 'odt'],
            'csv': ['csv'],
        }]


    def get_file(self):
        self.filepath = filedialog.askopenfilename()
        self.filename = self.filepath.split('/')[-1]
        self.create_dataframe()
        return self.filename


    def create_dataframe(self):
        file_extension = self.filename.split('.')[-1]
        for extension in self.good_extensions:
            if len(self.data_types_in_cols) > 0:
                self.data_types_in_cols = {}
            if file_extension in extension['excel']:
                self.df = pd.read_excel(self.filepath)
                self.columns = self.df.columns.values
                self.get_cols_datatypes()
            elif file_extension in extension['csv']:
                self.df = pd.read_csv(self.filepath)
                self.columns = self.df.columns.values
                self.get_cols_datatypes()
            else:
                print('wrong file extension')
        return self.columns


    def get_cols_datatypes(self):
        for i in self.columns:
            self.data_types_in_cols[i] = self.df[i].dtype


    def unique_values(self, columns):
        unique_values = {}
        if len(columns) > 0:
            for column in columns:
                unique = self.df[column].unique()
                unique_values[column] = unique
            return unique_values
        else:
            return None