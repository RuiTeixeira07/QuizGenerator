from xml.etree import ElementTree as ET
from QuizGenerator.generator.format.format import Format
from QuizGenerator.model.question import Question
from QuizGenerator.model.type import MULTIPLE_CHOICE, TRUE_OR_FALSE

text_tag = "text"
name_tag = "name"
question_text_tag = "questiontext"

answer_tag = "answer"
correct_answer_fraction = "100"
wrong_multiple_choice_answer_fraction = "0"
wrong_true_or_false_answer_fraction = "-25"

shuffle_answers_tag = "shuffleanswers"
shuffle_answers_active_tag = "1"

class GeneratorExtensions:
    @staticmethod
    def create_element_containing_text_element(
        question_element: ET.Element[str],
        element_tag: str,
        text: str,
        fraction: str = None) -> None:
        if fraction is not None:
            element = ET.SubElement(question_element, element_tag, fraction=fraction)
        else:
            element = ET.SubElement(question_element, element_tag)

        ET.SubElement(element, text_tag).text = text

    @staticmethod
    def create_common_question_tags(question_element: ET.Element[str], question: Question) -> None:
        GeneratorExtensions.create_element_containing_text_element(question_element, name_tag, question.id)

        GeneratorExtensions.create_element_containing_text_element(
            question_element,
            question_text_tag,
            Format.format_text_to_display(question.text))

        ET.SubElement(question_element, shuffle_answers_tag).text = shuffle_answers_active_tag

    @staticmethod
    def create_type_specific_question_tags(question_element: ET.Element[str], question: Question) -> None:
        """
        Create type-specific question tags.
        Correct answer is specified first.

        :param ET.Element[str] question_element: The question element.
        :param Question question: The question object.
        """

        GeneratorExtensions.__create_correct_answer_tags(question_element, question)
        GeneratorExtensions.__create_wrong_answer_tags(question_element, question)

    @staticmethod
    def __create_wrong_answer_tags(question_element: ET.Element[str], question: Question) -> None:
         for wrong_answer in question.wrong_answers:
             match question.type.value:
                 case MULTIPLE_CHOICE.value:
                     GeneratorExtensions.create_element_containing_text_element(
                         question_element,
                         answer_tag,
                         wrong_answer.value,
                         wrong_multiple_choice_answer_fraction)

                 case TRUE_OR_FALSE.value:
                     GeneratorExtensions.create_element_containing_text_element(
                         question_element,
                         answer_tag,
                         wrong_answer.value.lower(),
                         wrong_true_or_false_answer_fraction)

    @staticmethod
    def __create_correct_answer_tags(question_element: ET.Element[str], question: Question) -> None:
        for correct_answer in question.correct_answers:
            match question.type.value:
                case MULTIPLE_CHOICE.value:
                    GeneratorExtensions.create_element_containing_text_element(
                        question_element,
                        answer_tag,
                        correct_answer.value,
                        correct_answer_fraction)

                case TRUE_OR_FALSE.value:
                    GeneratorExtensions.create_element_containing_text_element(
                        question_element,
                        answer_tag,
                        correct_answer.value.lower(),
                        correct_answer_fraction)