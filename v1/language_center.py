# HERE GOES DATA FOR LANGUAGES AND LANGUAGE TRANSLATION
# MAKE IT A CLASS


languages = {
    'eng': {
        'LOAD FILE': 'Load File',
        "File name:": "File name:",
        'CHANGE FILE': 'CHANGE FILE',
        'SHOW TABLE': 'SHOW TABLE',
        'SELECT COLUMN': 'SELECT COLUMN',
        'HIDE TABLE': 'HIDE ROWS',
        'HIDE COLUMNS': 'HIDE COLUMNS',
        'OK': 'OK',
        'get_highest_value': 'get_highest_value',
        'get_lowest_value': 'get_lowest_value',
        'get_average': 'get_average',
        'unique_values': 'unique_values',
        "The highest value in column ": "The highest value in column",
        'The lowest value in column ': 'The lowest value in column ',
        "HIDE": "HIDE",
        'The average value in column ': 'The average value in column ',
        'The median value in column ': 'The median value in column ',
        'get_median': 'get_median',
        'get_most_frequent': 'get_most_frequent',
        'The most frequent value in column ': 'The most frequent value in column ',
        "Error": "Error",
        "An error occurred": "An error occurred",
        'wrong file extension': 'wrong file extension',
        "get_standard_deviation": "get_standard_deviation",
        "The standard deviation value in column ": "The standard deviation value in column ",
        'get_variance': 'get_variance',
        'The variance in column ': 'The variance in column ',
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

    },
    'es': {
        'LOAD FILE': '___ES___',
        "File name:": '___ES___',
        'CHANGE FILE': '___ES___',
        'SHOW TABLE': '___ES___',
        'SELECT COLUMN': '___ES___',
        'HIDE TABLE': '___ES___',
        'HIDE COLUMNS': '___ES___',
        'OK': 'OK',
        'get_highest_value': '___ES___',
        'get_lowest_value': '___ES___',
        'get_average': '___ES___',
        'unique_values': '___ES___',
        "The highest value in column ": '___ES___',
        'The lowest value in column ': '___ES___',
        "HIDE": '___ES___',
        'The average value in column ': '___ES___',
        "get_median": '___ES___',
        'The median value in column ': '___ES___',
        'get_most_frequent': '___ES___',
        'The most frequent value in column ': '___ES___',
        "Error": '___ES___',
        "An error occurred": '___ES___',
        'wrong file extension': '___ES___',
        "get_standard_deviation": '___ES___',
        "The standard deviation value in column ": '___ES___',
        'get_variance': '___ES___',
        'The variance in column ': '___ES___',
    }
}


class LanguageCenter:
    def __init__(self):
        # HARD CODED FOR TESTING
        self.language = languages['eng']


    def translate(self, word):
        translated = self.language[word]
        return translated