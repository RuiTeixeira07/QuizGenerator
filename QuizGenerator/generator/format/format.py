import os
from xml.etree import ElementTree as ET

indent_size = 4 * " "

paragraph_placeholder = " ... "
open_paragraph_tag = "<p>"
close_paragraph_tag = "</p>"

class Format:
    @staticmethod
    def indent_element_tree(root: ET.Element[str]) -> None:
        ET.indent(root, space=indent_size)

    @staticmethod
    def format_text_to_display(text: str) -> str:
        formatted_text_list = text.split(paragraph_placeholder)

        formatted_text = formatted_text_list[0]

        for paragraph in formatted_text_list[1:]:
            formatted_text += open_paragraph_tag + paragraph + close_paragraph_tag

        return formatted_text

    @staticmethod
    def request_file_path(file_name: str, file_type: str, recommended_file_path: str, must_exist: bool = True) -> str:
        while True:
            file_path = input(f"Insert path to {file_name} (Recommended '{recommended_file_path}'): ").strip()

            if not file_path:
                file_path = recommended_file_path

            if not must_exist and file_path.upper().endswith(file_type.upper()):
                return file_path

            if must_exist and file_path.upper().endswith(file_type.upper()) and os.path.isfile(file_path):
                return file_path