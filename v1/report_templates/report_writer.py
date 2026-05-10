

class ReportWriter:
    def __init__(self, analysis_brain):
        self.analysis_brain = analysis_brain

        self.string_template = 'string.txt'
        self.numerical_template = 'numerical.txt'

        self.cols = self.analysis_brain.cols
        self.data_types = self.analysis_brain.data_types_in_cols

