import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk, filedialog
from popups import *
from report_writer import *


class AnalysisBrain:
    def __init__(self, lang_center):
        self.filepath = None
        self.filename = None
        self.columns = None
        self.df = None
        self.tree = None
        self.col_set_type = None
        self.column_selection_advanced = []
        self.final_selection_advanced_cols = []
        self.operations_per_col = {}
        self.data_types_in_cols = {}
        self.operation_buttons = []
        self.all_operations = {
            'unique_values': self.unique_values,
            'get_highest_value': self.get_highest_value,
            'get_lowest_value' : self.get_lowest_value,
            'get_average': self.get_average,
            'get_median': self.get_median,
            'get_standard_deviation': self.get_standard_deviation,
            'get_variance': self.get_variance,
            'get_most_frequent': self.get_most_frequent,
            'get_percentiles': self.get_percentiles,
        }
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
                self.get_cols_datatypes()

            elif file_extension in extension['csv']:
                self.df = pd.read_csv(self.filepath)
                self.columns = self.df.columns.values
                self.get_cols_datatypes()

            else:
                feedback('wrong file extension', self.lang_center)
                return None

        for col in self.columns:
            self.get_available_operations([col])

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
                operations = ['get_highest_value', 'get_lowest_value', 'get_average', 'get_median', 'get_most_frequent', 'get_standard_deviation', 'get_variance', 'get_percentiles']
                self.operations_per_col[column] = operations
                return operations
            elif 'float' in dtype:
                operations =  ['get_highest_value', 'get_lowest_value', 'get_average', 'get_median', 'get_most_frequent', 'get_standard_deviation', 'get_variance', 'get_percentiles']
                self.operations_per_col[column] = operations
                return operations
            elif 'str' in dtype.lower() or 'object' in dtype.lower() or 'string' in dtype.lower():
                operations =  ['unique_values', 'get_most_frequent']
                self.operations_per_col[column] = operations
                return operations
        return None


    def unique_values(self, column):
        unique_values = {}
        if len(column) > 0 and isinstance(column, str):
            counts = self.df[column].value_counts()
            unique_values = counts.to_dict()
            if self.is_all_unique(column):
                return 'all values are unique'
            if self.is_all_same(column):
                return 'all values are same'
            else:
                return unique_values
        else:
            print('wrong column')
            return None

    def is_all_unique(self, column):
        return self.df[column].nunique() == len(self.df[column])

    def is_all_same(self, column):
        return self.df[column].nunique() == 1


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


    def get_variance(self, column):
        var = self.df[column].var()
        return var


    def get_most_frequent(self, column):
        modes = self.df[column].mode()
        # print(most_frequent)
        if self.is_all_same(column):
            return 'All values are the same'
        elif len(modes) > 1:
            return 'Equal frequency.'
        else:
            return modes[0]


    def get_percentiles(self, column):

        q1 = self.df[column].quantile(0.25)
        q3 = self.df[column].quantile(0.75)
        iqr = q3 - q1

        percentiles = {'Q1': q1, 'Q3': q3, 'IQR': iqr}

        return percentiles


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

