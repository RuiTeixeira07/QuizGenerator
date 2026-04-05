import csv
import os

file_extension = ".CSV"
file_delimiter = ';'
read_mode = "r"

class File:
    def __init__(self: File, file_path: str):
        self.file_path = file_path

    def read_file(self: File) -> list[dict[str, str]]:
        if not self.file_path.casefold().endswith(file_extension.casefold()):
            raise ValueError("Invalid File: '{}'. Required Comma-separated Values.".format(self.file_path))

        if not os.path.isfile(self.file_path):
            raise FileNotFoundError("File Not Found: '{}'.".format(self.file_path))

        with open(self.file_path, read_mode) as file:
            reader = csv.DictReader(file, delimiter=file_delimiter)
            return list(reader)