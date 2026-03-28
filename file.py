import csv

class File:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                reader = csv.DictReader(file, delimiter=';')
                return list(reader)

        except FileNotFoundError:
            print("File not found: {}".format(self.file_path))
            return []