import csv

file_delimiter = ';'
read_mode = "r"

class File:
    def __init__(self: File, file_path: str):
        self.file_path = file_path

    def read_file(self: File) -> list[dict[str, str]]:
        try:
            with open(self.file_path, read_mode) as file:
                reader = csv.DictReader(file, delimiter=file_delimiter)
                return list(reader)

        except FileNotFoundError:
            print("File Not Found: {}".format(self.file_path))
            return []