from xml.etree import ElementTree as ET
from QuizGenerator.generator.format.format import Format
from QuizGenerator.model.question import Question
from QuizGenerator.model.type import Type, MULTIPLE_CHOICE, TRUE_OR_FALSE

indent_size = 4 * " "
write_bytes_mode = "wb"
default_encoding = "utf-8"

root_tag = "quiz"
question_tag = "question"
name_tag = "name"
text_tag = "text"
question_text_tag = "questiontext"

answer_tag = "answer"
correct_answer_fraction = "100"
wrong_multiple_choice_answer_fraction = "0"
wrong_true_or_false_answer_fraction = "-25"

shuffle_answers_tag = "shuffleanswers"
shuffle_answers_active_tag = "1"

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

        Generator.__indent_element_tree(root)

        return root

    @staticmethod
    def __indent_element_tree(root: ET.Element[str]) -> None: ET.indent(root, space=indent_size)

    @staticmethod
    def __create_question_tag(root: ET.Element[str], question: Question) -> None:
        question_element = ET.SubElement(root, question_tag, type=Type.translate_type(question.type).value)

        Generator.__create_common_question_tags(question_element, question)
        Generator.__create_type_specific_question_tags(question_element, question)

    @staticmethod
    def __create_common_question_tags(question_element: ET.Element[str], question: Question) -> None:
        Generator.__create_element_containing_text_element(question_element, name_tag, question.id)

        Generator.__create_element_containing_text_element(
            question_element,
            question_text_tag,
            Format.format_text(question.text))

        ET.SubElement(question_element, shuffle_answers_tag).text = shuffle_answers_active_tag

    @staticmethod
    def __create_type_specific_question_tags(question_element: ET.Element[str], question: Question) -> None:
        for correct_answer in question.correct_answers:
            match question.type.value:
                case MULTIPLE_CHOICE.value:
                    Generator.__create_element_containing_text_element(
                        question_element,
                        answer_tag,
                        correct_answer.value,
                        correct_answer_fraction)

                case TRUE_OR_FALSE.value:
                    Generator.__create_element_containing_text_element(
                        question_element,
                        answer_tag,
                        correct_answer.value.lower(),
                        correct_answer_fraction)

        for wrong_answer in question.wrong_answers:
            match question.type.value:
                case MULTIPLE_CHOICE.value:
                    Generator.__create_element_containing_text_element(
                        question_element,
                        answer_tag,
                        wrong_answer.value,
                        wrong_multiple_choice_answer_fraction)

                case TRUE_OR_FALSE.value:
                    Generator.__create_element_containing_text_element(
                        question_element,
                        answer_tag,
                        wrong_answer.value.lower(),
                        wrong_true_or_false_answer_fraction)

    @staticmethod
    def __create_element_containing_text_element(
        question_element: ET.Element[str],
        element_tag: str,
        text: str,
        fraction: str = None) -> None:
        if fraction is not None:
            element = ET.SubElement(question_element, element_tag, fraction=fraction)
        else:
            element = ET.SubElement(question_element, element_tag)

        ET.SubElement(element, text_tag).text = text

    def __write_file(self: Generator, root: ET.Element[str]) -> None:
        with open(self.quiz_path, write_bytes_mode) as file:
            file.write(ET.tostring(root, encoding=default_encoding, xml_declaration=True))