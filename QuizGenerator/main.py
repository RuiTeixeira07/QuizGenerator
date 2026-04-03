from QuizGenerator.file.file import File
from QuizGenerator.generator.format.format import Format
from QuizGenerator.generator.generator import Generator
from QuizGenerator.model.question import Question

questions_data_path_extension = ".CSV"
generated_quiz_path_extension = ".XML"

questions_data_path = f"assets/QuestionsData{questions_data_path_extension.upper()}"
generated_quiz_path = f"quiz/Quiz{generated_quiz_path_extension.upper()}"

class Main:
    @staticmethod
    def run() -> None:
        questions_data = File(Format.request_file_path("Questions Data", questions_data_path_extension, questions_data_path)).read_file()
        questions = Question.create_questions(questions_data)
        Generator(Format.request_file_path("Generated Quiz", generated_quiz_path_extension, generated_quiz_path, False)).generate_quiz(questions)
        print("Quiz Generated!")

if __name__ == '__main__':
    main = Main()
    main.run()