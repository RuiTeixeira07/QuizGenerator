from QuizGenerator.file import File
from QuizGenerator.model.question import Question

questions_data_path = '../assets/QuestionsData.csv'

class Main:
    @staticmethod
    def run():
        questions_data = File(questions_data_path).read_file()
        questions = Question.create_questions(questions_data)

        for question in questions:
            print(question)

if __name__ == '__main__':
    main = Main()
    main.run()