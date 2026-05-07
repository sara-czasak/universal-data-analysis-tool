# HERE GOES DATA FOR LANGUAGES AND LANGUAGE TRANSLATION
# MAKE IT A CLASS


languages = {
    'eng': {
        'LOAD FILE': 'Load File',
        "File name:": "File name:",
        'CHANGE FILE': 'CHANGE FILE',
        'SHOW FIRST 5 ROWS': 'SHOW FIRST 5 ROWS',
        'SELECT COLUMNS': 'SELECT COLUMNS',
        'HIDE ROWS': 'HIDE ROWS',
        'HIDE COLUMNS': 'HIDE COLUMNS',
    },
    'pl': {
        'LOAD FILE': '___PL___',
        "File name:": '___PL___',
        'CHANGE FILE': '___PL___',
        'SHOW FIRST 5 ROWS': '___PL___',
        'SELECT COLUMNS': '___PL___',
        'HIDE ROWS': '___PL___',
        'HIDE COLUMNS': '___PL___',
    },
    'es': {
        'LOAD FILE': '___ES___',
        "File name:": '___ES___',
        'CHANGE FILE': '___ES___',
        'SHOW FIRST 5 ROWS': '___ES___',
        'SELECT COLUMNS': '___ES___',
        'HIDE ROWS': '___ES___',
        'HIDE COLUMNS': '___ES___',
    }
}


class LanguageCenter:
    def __init__(self):
        # HARD CODED FOR TESTING
        self.language = languages['eng']


    def translate(self, word):
        translated = self.language[word]
        return translated