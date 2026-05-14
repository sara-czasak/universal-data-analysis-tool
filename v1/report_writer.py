import tkinter as tk
from tkinter import ttk, filedialog, simpledialog
from popups import *


class ReportWriter:
    def __init__(self, analysis_brain):
        self.analysis_brain = analysis_brain

        self.string_template = None
        self.numerical_template = None
        self.save_path = None
        self.name = None
        self.report = None


    # save_type: basic, advanced
    def check_if_path_exists_and_set_up_file(self, save_type):
        if self.save_path is None:
            self.ask_filename()

        if save_type == 'basic':
            self.get_report_data()
            self.get_report_templates()
            self.set_file_header()
            self.write_report_file()

        elif save_type == 'advanced':
            self.get_sub_df()


    def get_report_templates(self):
        with open('report_templates/string.txt', 'r') as f:
            self.string_template = f.readlines()
        with open('report_templates/numerical.txt', 'r') as f:
            self.numerical_template = f.readlines()


    def ask_filename(self):
        import os

        self.save_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=(('Text Files', '*.txt'),))
        if not self.save_path:
            return
        self.name = self.save_path.split('/')[-1].split('.')[0]

        dir_path = '/'.join(self.save_path.split('/')[:-1]) + '/' + self.name
        os.makedirs(dir_path, exist_ok=True)

        self.save_path = dir_path + '/' + self.name + '.txt'


    def get_nan_percentage(self, column):
        nan_count = self.analysis_brain.df[column].isna().sum()
        total = len(self.analysis_brain.df[column])
        nan_percentage = (nan_count / total) * 100
        return round(nan_percentage, 2)


    def get_report_data(self):
        report = {}

        for col_name, operations in self.analysis_brain.operations_per_col.items():
            col_data = {}
            col_data['type'] = self.analysis_brain.data_types_in_cols[col_name]
            report[col_name] = col_data
            for operation in operations:
                result = self.analysis_brain.all_operations[operation](col_name)

                if isinstance(result, dict):
                    result = {k: v.item() if hasattr(v, 'item') else v for k, v in result.items()}
                elif hasattr(result, 'item'):
                    result = result.item()

                col_data[operation] = result

            actual_data_percentage = 100 - self.get_nan_percentage(col_name)

            col_data['actual_data_percentage'] = actual_data_percentage
            col_data['nan_percentage'] = self.get_nan_percentage(col_name)

        self.report = report


    def write_report_file(self):
        for col_name, col_data in self.report.items():
            dtype = str(col_data['type'])
            if 'int' in dtype.lower() or 'float' in dtype.lower():
                self.fill_out_templates(col_name, col_data, 'numerical')
            elif 'str' in dtype.lower() or 'object' in dtype.lower():
                self.fill_out_templates(col_name, col_data, 'string')


    def set_file_header(self):
        with open(self.save_path, mode='a') as file:
            file.write(self.name + '\n\n')


    def fill_out_templates(self, col_name, col_data, type_of_data):
        with open(self.save_path, mode='a') as file:
            if type_of_data == 'numerical':
                for line in self.numerical_template:
                    for key, value in col_data.items():
                        if isinstance(value, dict):
                            for k, v in value.items():
                                line = line.replace(k.lower(), str(v))
                        else:
                            line =line.replace(key, str(value))

                    line = line.replace('col_name', col_name)
                    file.write(line)

            elif type_of_data == 'string':
                for line in self.string_template:
                    for key, value in col_data.items():
                        if isinstance(value, dict):
                            unique_block = '\n'.join(f'    {k}: {v}' for k, v in value.items())
                            line = line.replace(key, '\n' + unique_block)
                        else:
                            line = line.replace(key, str(value))

                    line = line.replace('col_name', col_name)
                    file.write(line)
            file.write('\n\n')


    def get_sub_df(self):
        subdf = self.analysis_brain.advanced_df.copy()
        if not subdf.empty:
            data_type_subdf = self.analysis_brain.col_set_type
            self.add_needed_cols(subdf, data_type_subdf)
            self.save_sub_df(subdf)
        else:
            return


    def add_needed_cols(self, subdf, data_type_subdf):
        if data_type_subdf is None:
            return
        elif data_type_subdf == 'num':
            subdf['sum'] = subdf.sum(axis=1)
            subdf['mean'] = subdf.mean(axis=1)
            subdf['median'] = subdf.median(axis=1)
        elif data_type_subdf == 'str':
            subdf['concat'] = subdf.apply(
                lambda row: ' '.join(row.fillna('').astype(str)), axis=1
            )


    def save_sub_df(self, subdf):
        name = simpledialog.askstring(self.analysis_brain.lang_center.translate("Filename"), self.analysis_brain.lang_center.translate("Enter filename (without extension):"))
        if not name:
            return
        sheet_name = name + '.xlsx'
        sheet_path = '/'.join(self.save_path.split('/')[:-1]) + '/' + sheet_name

        subdf.to_excel(sheet_path, index=False)
        feedback('Data saved successfully', self.analysis_brain.lang_center)
