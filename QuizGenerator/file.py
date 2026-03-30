import csv

file_delimiter = ';'

class File:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_file(self) -> list[dict[str, str]]:
        try:
            with open(self.file_path, 'r') as file:
                reader = csv.DictReader(file, delimiter=file_delimiter)
                return list(reader)

        except FileNotFoundError:
            print("File Not Found: {}".format(self.file_path))
            return []