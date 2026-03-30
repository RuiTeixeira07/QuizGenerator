from dataclasses import dataclass

concatenated_answers_delimiter = "|"

@dataclass(frozen=True)
class Answer:
    value: str

    @staticmethod
    def create_answers(concatenated_answers: str) -> list[Answer]:
        answers = concatenated_answers.split(concatenated_answers_delimiter)
        answers_list = []

        for answer in answers:
            answers_list.append(Answer(answer))

        return answers_list