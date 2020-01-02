import os

from src.CompImage import CompetitionImage


class ImageManager:

    FILE_TYPES = ['.png', '.jpg', '.jpeg']

    def __init__(self, image_folder):
        self.images = self.retrieve_images(image_folder)
        self.held_images = []
        self.pointer = 0

    def next(self):
        print("Next")
        self.pointer += 1

    def get_image_path(self):
        print(f"path={self.images[self.pointer].file_path}")
        return self.images[self.pointer].file_path

    def get_image_title(self):
        print(f"title={self.images[self.pointer].title}")
        return self.images[self.pointer].title

    def save_score(self, score):
        print(f"saving score of {score}")
        self.images[self.pointer].score = score

    def hold(self):
        self.held_images.append(self.images[self.pointer])

    def retrieve_images(self, path):
        images = []
        for dirpath, _, files in os.walk(path):
            for file in files:
                file_name, file_extension = os.path.splitext(file)
                if file_extension.lower() in self.FILE_TYPES:
                    full_path = os.path.join(dirpath, file)
                    img = CompetitionImage(full_path, file_name)
                    images.append(img)
        return images
