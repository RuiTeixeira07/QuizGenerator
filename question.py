from dataclasses import dataclass
from model.answer import Answer
from model.difficulty import Difficulty, EMPTY as DIFFICULTY_EMPTY
from model.type import Type, EMPTY as TYPE_EMPTY

id_tag = "ID"
difficulty_tag = "Difficulty"
text_tag = "Question"
type_tag = "Question Type"
wrong_answers_tag = "Wrong Answers"
correct_answers_tag = "Correct Answers"

@dataclass(frozen=True)
class Question:
    id: str
    difficulty: Difficulty
    text: str
    type: Type
    wrong_answers: list[Answer]
    correct_answers: list[Answer]

    @classmethod
    def create_questions(cls, questions_data: list[dict[str, str]]) -> list[Question]:
        questions = []

        for question_data in questions_data:
            question = cls.__create_question_from_dictionary(question_data)

            if cls.__question_is_valid(question):
                questions.append(question)

        return questions

    @classmethod
    def __question_is_valid(cls, question: Question) -> bool:
        return (question.id is not None
                and question.difficulty != DIFFICULTY_EMPTY
                and question.text is not None
                and question.type != TYPE_EMPTY
                and question.wrong_answers
                and question.correct_answers)

    @classmethod
    def __create_question_from_dictionary(cls, question_data: dict[str, str]) -> Question:
        return Question(
            cls.__get_from_tag(question_data, id_tag),
            Difficulty.create_difficulty_from(cls.__get_from_tag(question_data, difficulty_tag)),
            cls.__get_from_tag(question_data, text_tag),
            Type.create_type_from(cls.__get_from_tag(question_data, type_tag)),
            Answer.create_answers(cls.__get_from_tag(question_data, wrong_answers_tag)),
            Answer.create_answers(cls.__get_from_tag(question_data, correct_answers_tag)))

    @classmethod
    def __get_from_tag(cls, question_data: dict[str, str], tag: str) -> str:
        return question_data[tag] if tag in question_data else None