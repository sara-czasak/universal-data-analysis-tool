# HERE GOES DATA FOR LANGUAGES AND LANGUAGE TRANSLATION
# MAKE IT A CLASS


languages = {
    'eng': {
        'Load File': 'Load File',
        "File name:": "File name:",

    },
    'pl': {
        'Load File': '',
        "File name:": "",

    },
    'es': {
        'Load File': '',
        "File name:": "",
    }
}


class LanguageCenter:
    def __init__(self):
        # HARD CODED FOR TESTING
        self.language = languages['eng']
        self.languages = {
    'eng': {
        'Load File': 'Load File',
        "File name:": "File name:",

    },
    'pl': {
        'Load File': '',
        "File name:": "",

    },
    'es': {
        'Load File': '',
        "File name:": "",
    }
}


    def translate(self, word):
        translated = self.language[word]
        return translated