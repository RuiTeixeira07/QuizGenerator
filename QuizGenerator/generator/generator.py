from xml.etree import ElementTree as ET
from QuizGenerator.generator.extensions.extensions import GeneratorExtensions
from QuizGenerator.generator.format.format import Format
from QuizGenerator.model.question import Question
from QuizGenerator.model.type import Type

write_bytes_mode = "wb"
default_encoding = "utf-8"

root_tag = "quiz"
question_tag = "question"

class Generator:
    def __init__(self: Generator, quiz_path: str):
        self.quiz_path = quiz_path

    def generate_quiz(self: Generator, questions: list[Question]) -> None:
        root = self.__create_element_tree(questions)
        self.__write_file(root)

    @staticmethod
    def __create_element_tree(questions: list[Question]) -> ET.Element[str]:
        root = ET.Element(root_tag)

        for question in questions:
            Generator.__create_question_tag(root, question)

        Format.indent_element_tree(root)

        return root

    @staticmethod
    def __create_question_tag(root: ET.Element[str], question: Question) -> None:
        question_element = ET.SubElement(root, question_tag, type=Type.translate_type(question.type).value)

        GeneratorExtensions.create_common_question_tags(question_element, question)
        GeneratorExtensions.create_type_specific_question_tags(question_element, question)

    def __write_file(self: Generator, root: ET.Element[str]) -> None:
        with open(self.quiz_path, write_bytes_mode) as file:
            file.write(ET.tostring(root, encoding=default_encoding, xml_declaration=True))