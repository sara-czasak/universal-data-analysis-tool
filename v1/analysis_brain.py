import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk, filedialog
from popups import *


class AnalysisBrain:
    def __init__(self, lang_center):
        self.filepath = None
        self.filename = None
        self.columns = None
        self.df = None
        self.tree = None
        self.data_types_in_cols = {}
        self.operation_buttons = []
        self.good_extensions = [{
            'excel': ['xls', 'xlsx', 'xlsm', 'xlsb', 'odf', 'ods', 'odt'],
            'csv': ['csv'],
        }]
        self.root = None
        self.lang_center = lang_center


    def get_file(self, root):
        if self.filepath is None:
            self.root = root
            self.filepath = filedialog.askopenfilename()
            if self.filepath == '':
                self.filepath = None
                return None
            self.filename = self.filepath.split('/')[-1]
            result = self.create_dataframe()
            if result is None:
                self.file_reset()
                return None
            return self.filename
        else:
            self.file_reset()
            self.filepath = filedialog.askopenfilename()
            if self.filepath == '':
                self.filepath = None
                return None
            self.filename = self.filepath.split('/')[-1]
            result = self.create_dataframe()
            if result is None:
                self.file_reset()
                return None
            return self.filename


    def create_dataframe(self):
        file_extension = self.filename.split('.')[-1]
        for extension in self.good_extensions:
            if len(self.data_types_in_cols) > 0:
                self.data_types_in_cols = {}
            if file_extension in extension['excel']:
                self.df = pd.read_excel(self.filepath)
                self.columns = list(self.df.columns)
                # self.columns = self.df.columns.values
                self.get_cols_datatypes()
            elif file_extension in extension['csv']:
                self.df = pd.read_csv(self.filepath)
                self.columns = self.df.columns.values
                self.get_cols_datatypes()
            else:
                feedback('wrong file extension', self.lang_center)
                return None
        return self.columns


    def get_cols_datatypes(self):
        for i in self.columns:
            if self.df[i].dtype == object:
                self.data_types_in_cols[i] = 'str'
            else:
                self.data_types_in_cols[i] = self.df[i].dtype


    def get_available_operations(self, columns):
        for column in columns:
            dtype = str(self.data_types_in_cols[column])
            if 'int' in dtype:
                return ['get_highest_value', 'get_lowest_value', 'get_average', 'get_median', 'get_most_frequent', 'get_standard_deviation']
            elif 'float' in dtype:
                return ['get_highest_value', 'get_lowest_value', 'get_average', 'get_median', 'get_most_frequent', 'get_standard_deviation']
            elif 'str' in dtype.lower() or 'object' in dtype.lower() or 'string' in dtype.lower():
                return ['unique_values', 'get_most_frequent']
        return None


    def unique_values(self, column):
        unique_values = {}
        if len(column) > 0 and isinstance(column, str):
            counts = self.df[column].value_counts()
            unique_values = counts.to_dict()
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


    def get_average(self, column):
        average = self.df[column].mean()
        return average


    def get_median(self, column):
        median = self.df[column].median()
        return median


    def get_standard_deviation(self, column):
        std = self.df[column].std()
        return std


    def get_most_frequent(self, column):
        most_frequent = self.df[column].mode()[0]
        return most_frequent


    def file_reset(self):
        for button in self.operation_buttons:
            button.destroy()


        self.filepath = None
        self.filename = None
        self.columns = None
        self.df = None
        self.tree = None
        self.data_types_in_cols = {}
        self.operation_buttons = []


    def get_rows(self, col_name, value):
        rows = self.df[self.df[col_name] == value]
        return rows
