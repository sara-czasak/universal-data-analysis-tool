from tkinter import ttk
from tkinter import *
from style_mgr import *


languages = {
    'eng': {
        'LOAD FILE': 'Load File',
        "File name:": "File name:",
        'CHANGE FILE': 'CHANGE FILE',
        'SHOW TABLE': 'SHOW TABLE',
        'SELECT COLUMN': 'SELECT COLUMN',
        'HIDE TABLE': 'HIDE TABLE',
        'HIDE COLUMNS': 'HIDE COLUMNS',
        'OK': 'OK',
        'get_highest_value': 'highest value',
        'get_lowest_value': 'lowest value',
        'get_average': 'average',
        'unique_values': 'unique values',
        "The highest value in column ": "The highest value in column",
        'The lowest value in column ': 'The lowest value in column ',
        "HIDE": "HIDE",
        'The average value in column ': 'The average value in column ',
        'The median value in column ': 'The median value in column ',
        'get_median': 'median',
        'get_most_frequent': 'most frequent',
        'The most frequent value in column ': 'The most frequent value in column ',
        "Error": "Error",
        "An error occurred": "An error occurred",
        'wrong file extension': 'wrong file extension',
        "get_standard_deviation": "standard deviation",
        "The standard deviation value in column ": "The standard deviation value in column ",
        'get_variance': 'variance',
        'The variance in column ': 'The variance in column ',
        'get_percentiles': 'percentiles',
        'GO TO\nADVANCED\nANALYSIS': 'GO TO\nADVANCED\nANALYSIS',
        'GO TO\nBASIC\nANALYSIS': 'GO TO\nBASIC\nANALYSIS',
        "Basic Analysis": 'Basic Analysis',
        "Advanced Analysis": 'Advanced Analysis',
        'SELECT COLUMNS': 'SELECT COLUMNS',
        'PLEASE SELECT AT LEAST TWO COLUMNS': 'PLEASE SELECT AT LEAST TWO COLUMNS',
        'sum_row_vals_in_columns': 'sum values in columns',
        'mean_row_vals_in_columns': 'mean values in columns',
        'median_row_vals_in_columns': 'median values in columns',
        'Save': 'Save',
        'Data saved successfully': 'Data saved successfully',
        'Filename': 'Filename',
        'Enter filename (without extension):': 'Enter filename (without extension):',
        'concat_row_vals_in_columns': 'join values',
        'Please select at least 2 columns': 'Please select at least 2 columns',
        'product_row_vals_in_columns': 'product of values in columns',
    },
    'pl': {
        'LOAD FILE': '___PL___',
        "File name:": '___PL___',
        'CHANGE FILE': '___PL___',
        'SHOW TABLE': '___PL___',
        'SELECT COLUMN': '___PL___',
        'HIDE TABLE': '___PL___',
        'HIDE COLUMNS': '___PL___',
        'OK': 'OK',
        'get_highest_value': '___PL___',
        'get_lowest_value': '___PL___',
        'get_average': '___PL___',
        'unique_values': '___PL___',
        "The highest value in column ": '___PL___',
        'The lowest value in column ': '___PL___',
        "HIDE": '___PL___',
        'The average value in column ': '___PL___',
        "get_median": '___PL___',
        'The median value in column ': '___PL___',
        'get_most_frequent': '___PL___',
        'The most frequent value in column ': '___PL___',
        "Error": '___PL___',
        "An error occurred": '___PL___',
        'wrong file extension': '___PL___',
        "get_standard_deviation": '___PL___',
        "The standard deviation value in column ": '___PL___',
        'get_variance': '___PL___',
        'The variance in column ': '___PL___',
        'get_percentiles': '___PL___',
        'GO TO\nADVANCED\nANALYSIS': '___PL___',
        'GO TO\nBASIC\nANALYSIS': '___PL___',
        "Basic Analysis": '___PL___',
        "Advanced Analysis": '___PL___',
        'SELECT COLUMNS': '___PL___',
        'PLEASE SELECT AT LEAST TWO COLUMNS': '___PL___',
        'sum_row_vals_in_columns': '___PL___',
        'mean_row_vals_in_columns': '___PL___',
        'median_row_vals_in_columns': '___PL___',
        'Save': '___PL___',
        'Data saved successfully': '___PL___',
        'Filename': '___PL___',
        'Enter filename (without extension):': '___PL___',
        'concat_row_vals_in_columns': '___PL___',
        'Please select at least 2 columns': '___PL___',
        'product_row_vals_in_columns': '___PL___',

    },
    'es': {
        'LOAD FILE': 'ABRIR ARCHIVO',
        "File name:": 'Nombre del archivo:',
        'CHANGE FILE': 'CAMBIAR ARCHIVO',
        'SHOW TABLE': 'MOSTRAR TABLA',
        'SELECT COLUMN': 'SELECCIONAR COLUMNA',
        'HIDE TABLE': 'OCULTAR TABLA',
        'HIDE COLUMNS': 'OCULTAR COLUMNAS',
        'OK': 'OK',
        'get_highest_value': 'obtener valor más alto',
        'get_lowest_value': 'obtener valor más bajo',
        'get_average': 'obtener promedio',
        'unique_values': 'valores unicos',
        "The highest value in column ": 'El valor más alto en la columna ',
        'The lowest value in column ': 'El valor más bajo en la columna ',
        "HIDE": 'ESCONDER',
        'The average value in column ': 'El valor promedio en la columna ',
        "get_median": 'obtener mediana',
        'The median value in column ': 'El valor mediano en la columna ',
        'get_most_frequent': 'obtener más frecuente',
        'The most frequent value in column ': 'El valor más frecuente en la columna ',
        "Error": 'Error',
        "An error occurred": 'Se produjo un error',
        'wrong file extension': 'extensión de archivo incorrecta',
        "get_standard_deviation": 'get desviación estándar',
        "The standard deviation value in column ": 'El valor de la desviación estándar en la columna ',
        'get_variance': 'obtener varianza',
        'The variance in column ': 'La varianza en la columna ',
        'get_percentiles': 'obtener percentiles',
        'GO TO\nADVANCED\nANALYSIS': 'IR A\nANÁLISIS AVANZADO',
        'GO TO\nBASIC\nANALYSIS': 'IR A\nANÁLISIS BÁSICO',
        "Basic Analysis": 'Análisis básico',
        "Advanced Analysis": 'Análisis avanzado',
        'SELECT COLUMNS': 'SELECCIONAR COLUMNAS',
        'PLEASE SELECT AT LEAST TWO COLUMNS': 'POR FAVOR SELECCIONE AL MENOS DOS COLUMNAS',
        'sum_row_vals_in_columns': 'suma valores',
        'mean_row_vals_in_columns': 'valores promedios',
        'median_row_vals_in_columns': 'mediana',
        'Save': 'Guardar',
        'Data saved successfully': 'Datos guardados exitosamente',
        'Filename': 'Nombre del archivo',
        'Enter filename (without extension):': 'Nombre del archivo (sin extensión)',
        'concat_row_vals_in_columns': 'unir valores',
        'Please select at least 2 columns': 'Por favor seleccione al menos 2 columnas',
        'product_row_vals_in_columns': 'valores de productos',

    }
}


class LanguageCenter:
    def __init__(self):
        # HARD CODED FOR TESTING
        # self.language = languages['eng']
        self.language = None


    def choose_language(self, root):
        lang_screen = Toplevel(root)
        lang_screen.attributes('-topmost', True)
        lang_screen.title("Choose language")

        lang_screen.protocol("WM_DELETE_WINDOW", root.destroy)

        my_style = StyleWidgets(lang_screen)

        label = ttk.Label(lang_screen, text="Choose Language")
        label.pack(padx=5, pady=5)

        eng_button = ttk.Button(lang_screen, text="ENG", command=lambda: self.set_lang('eng', root=lang_screen))
        eng_button.pack(padx=10, pady=10)
        # pl_button = ttk.Button(lang_screen, text="PL", command=lambda: self.set_lang('pl', root=lang_screen))
        # pl_button.pack(padx=10, pady=10)
        es_button = ttk.Button(lang_screen, text="ES", command=lambda: self.set_lang('es', root=lang_screen))
        es_button.pack(padx=10, pady=10)

        lang_screen.grab_set()
        lang_screen.wait_window()


    def set_lang(self, lang, root):
        self.language = languages[lang]
        root.destroy()


    def translate(self, word):
        if self.language is None:
            return
        else:
            translated = self.language[word]
            return translated