import os
import re

class Corpus:
    def __init__(self, path):
        self.path = path

    def emails(self):
        for filename in os.listdir(self.path):
            file_path = os.path.join(self.path, filename)
            file_content = self.readfile(file_path)
            yield filename, file_content

              
    def readfile(self, file_path):
        with open(file_path, mode="rt", encoding="utf-8") as f:
            content = f.read()
            formatted_content = content.lower()
            words =  re.findall("[a-z0-9]+", formatted_content)
        return words