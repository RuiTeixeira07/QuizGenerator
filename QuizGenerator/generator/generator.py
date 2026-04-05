import os.path
from QuizGenerator.model.difficulty import ALL as DIFFICULTY_ALL
from collections import defaultdict
from xml.etree import ElementTree as ET
from QuizGenerator.generator.extensions.extensions import GeneratorExtensions
from QuizGenerator.generator.format.format import Format
from QuizGenerator.model.difficulty import Difficulty
from QuizGenerator.model.question import Question
from QuizGenerator.model.type import Type

file_extension = ".XML"
write_bytes_mode = "wb"
default_encoding = "utf-8"

root_tag = "quiz"
difficulty_tag = "category"
question_tag = "question"

course_path_prefix = "$course$/"

class Generator:
    def __init__(self: Generator, quiz_path: str):
        self.quiz_path = quiz_path

    def generate_quiz(self: Generator, questions: list[Question]) -> None:
        root = self.__create_element_tree(questions)
        self.__write_file(root)

    @staticmethod
    def __create_element_tree(questions: list[Question]) -> ET.Element[str]:
        root = ET.Element(root_tag)

        questions_by_difficulty = Generator.__group_questions_by_difficulty(questions)

        for difficulty in DIFFICULTY_ALL:
            if difficulty in questions_by_difficulty:
                Generator.__create_difficulty_tag(root, difficulty)

                for question in questions_by_difficulty[difficulty]:
                    Generator.__create_question_tag(root, question)

        Format.indent_element_tree(root)

        return root

    @staticmethod
    def __group_questions_by_difficulty(questions: list[Question]) -> defaultdict[Difficulty, list[Question]]:
        questions_by_difficulty = defaultdict(list)
        for question in questions:
            questions_by_difficulty[question.difficulty].append(question)

        return questions_by_difficulty

    @staticmethod
    def __create_difficulty_tag(root: ET.Element[str], difficulty: Difficulty) -> None:
        question_element = ET.SubElement(root, question_tag, type=difficulty_tag)

        GeneratorExtensions.create_element_containing_text_element(
            question_element,
            difficulty_tag,
            f"{course_path_prefix}{difficulty.value}")

    @staticmethod
    def __create_question_tag(root: ET.Element[str], question: Question) -> None:
        question_element = ET.SubElement(root, question_tag, type=Type.translate_type(question.type).value)

        GeneratorExtensions.create_common_question_tags(question_element, question)
        GeneratorExtensions.create_type_specific_question_tags(question_element, question)

    def __write_file(self: Generator, root: ET.Element[str]) -> None:
        if not self.quiz_path.casefold().endswith(file_extension.casefold()):
            raise ValueError("Invalid File: '{}'. Required XML.".format(self.quiz_path))

        if not os.path.exists(self.quiz_path):
            directory_path = os.path.dirname(os.path.abspath(self.quiz_path))
            os.makedirs(directory_path)

        with open(self.quiz_path, write_bytes_mode) as file:
            file.write(ET.tostring(root, encoding=default_encoding, xml_declaration=True))