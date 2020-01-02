import os


class CompetitionImage:

    SEPARATOR = '_'

    def __init__(self, path, file_name):
        self.file_path = path
        self.file_name = file_name
        self.title, self.photographer = self.get_image_details(file_name)
        self.score = None

    def get_image_details(self, file_name):
        details = file_name.split(self.SEPARATOR)
        return details[0], details[1]

    def score(self, score):
        self.score = score
