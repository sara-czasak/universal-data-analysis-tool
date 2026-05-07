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
        self.operation_buttons = []


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
            if self.df[i].dtype == object:
                self.data_types_in_cols[i] = 'str'
            else:
                self.data_types_in_cols[i] = self.df[i].dtype


    def get_available_operations(self, columns):
        for column in columns:
            if self.data_types_in_cols[column] == int:
                allowed_operations = ['get_highest_value', 'get_lowest_value']
                return allowed_operations
            elif self.data_types_in_cols[column] == float:
                allowed_operations = ['get_highest_value', 'get_lowest_value']
                return allowed_operations
            elif self.data_types_in_cols[column] == 'str':
                allowed_operations = ['unique_values']
                return allowed_operations
        else:
            return None


    def unique_values(self, column):
        unique_values = {}
        if len(column) > 0 and isinstance(column, str):
            counts = self.df[column].value_counts()
            unique_values = counts.to_dict()
            print(unique_values)
            return unique_values
        else:
            print('wrong column')
            return None


    def get_highest_value(self, column):
        highest_value = self.df[column].max()
        return highest_value


    def get_lowest_value(self, column):
        lowest_value = self.df[column].min()
        return lowest_value