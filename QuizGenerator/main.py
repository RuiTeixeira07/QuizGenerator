from QuizGenerator.file.file import File
from QuizGenerator.generator.generator import Generator
from QuizGenerator.model.question import Question

questions_data_path = "assets/QuestionsData.csv"
generated_quiz_path = "quiz/Quiz.xml"

class Main:
    @staticmethod
    def run() -> None:
        questions_data = File(questions_data_path).read_file()
        questions = Question.create_questions(questions_data)
        Generator(generated_quiz_path).generate_quiz(questions)

if __name__ == '__main__':
    main = Main()
    main.run()