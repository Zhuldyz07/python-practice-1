import os

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        if os.path.exists(self.filename):
            return True
        return False


    def create_output_folder(self, folder="output"):
        if not os.path.exists(folder):
            os.makedirs(folder)