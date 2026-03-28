from file import File

questions_data_path = 'assets/questionsData.csv'

class Main:
    @staticmethod
    def run():
        questions_data = File(questions_data_path).read_file()

        for question in questions_data:
            print(question)

if __name__ == '__main__':
    main = Main()
    main.run()