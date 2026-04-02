from dataclasses import dataclass
from QuizGenerator.model.answer import Answer
from QuizGenerator.model.difficulty import Difficulty, EMPTY as DIFFICULTY_EMPTY
from QuizGenerator.model.type import Type, EMPTY as TYPE_EMPTY

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

    @staticmethod
    def create_questions(questions_data: list[dict[str, str]]) -> list[Question]:
        questions = []

        for question_data in questions_data:
            question = Question.__create_question_from_dictionary(question_data)

            if not Question.__question_is_valid(question):
                print("Invalid Question: {}".format(question))
                continue

            questions.append(question)
        return questions

    @classmethod
    def __create_question_from_dictionary(cls: Question, question_data: dict[str, str]) -> Question:
        return Question(
            cls.__get_from_tag(question_data, id_tag),
            Difficulty.create_difficulty_from(cls.__get_from_tag(question_data, difficulty_tag)),
            cls.__get_from_tag(question_data, text_tag),
            Type.create_type_from(cls.__get_from_tag(question_data, type_tag)),
            Answer.create_answers(cls.__get_from_tag(question_data, wrong_answers_tag)),
            Answer.create_answers(cls.__get_from_tag(question_data, correct_answers_tag)))

    @staticmethod
    def __question_is_valid(question: Question) -> bool:
        return (question.id is not None
                and question.difficulty != DIFFICULTY_EMPTY
                and question.text is not None
                and question.type != TYPE_EMPTY
                and question.wrong_answers and len(question.wrong_answers) >= 1
                and question.correct_answers and len(question.correct_answers) >= 1)

    @staticmethod
    def __get_from_tag(question_data: dict[str, str], tag: str) -> str:
        return question_data[tag] if tag in question_data else None