import time
import requests
all_questions = {
    "What is the capital of France?": {
        "options": {
            "A": "Madrid",
            "B": "Berlin",
            "C": "Paris",
            "D": "Lisbon"
        },
        "answer": "C"
    },
    "Which planet is known as the Red Planet?": {
        "options": {
            "A": "Earth",
            "B": "Mars",
            "C": "Jupiter",
            "D": "Venus"
        },
        "answer": "B"
    },
    "Who wrote 'Hamlet'?": {
        "options": {
            "A": "Charles Dickens",
            "B": "William Shakespeare",
            "C": "Leo Tolstoy",
            "D": "Mark Twain"
        },
        "answer": "B"
    },
    "What is the largest mammal?": {
        "options": {
            "A": "African Elephant",
            "B": "Blue Whale",
            "C": "Giraffe",
            "D": "Hippopotamus"
        },
        "answer": "B"
    },
    "In which year did the Titanic sink?": {
        "options": {
            "A": "1912",
            "B": "1905",
            "C": "1898",
            "D": "1923"
        },
        "answer": "A"
    }
}


class Quiz:
    def __init__(self,current_player:str) -> None:
        self.current_player = current_player
    
    def print_welcome(self):

        """
        This func prints the user name and welcoming.

        """
        print(f""" Hello, {self.current_player}
        
Welcome to the Python Quiz Game!
You will be presented with multiple-choice questions. 
Enter the number corresponding to your answer.
""")
        
    def get_questions_from_api(self, amount=10, category=27, difficulty="hard", question_type="multiple"):
        """
        This func gets the questions from the api , takes the amount category and difficulty as variables so the player
        can change the difficulty or the number of questions
        """
        url = f"https://opentdb.com/api.php?amount={amount}&category={category}&difficulty={difficulty}&type={question_type}"
        response = requests.get(url)
        data = response.json()
        return data['results']
    
    def questions_from_api(self, amount=10, category=27, difficulty="hard", question_type="multiple"):
        """
        This func gets from the get question func the data and do a for loop for every question.
        this func indicates if the user is right or wrong and returns false at the end so we can proccess more actions later.
        """
        questions = self.get_questions_from_api(amount, category, difficulty, question_type)
        correct_answers = 0
        total_questions = len(questions)
        start_time = time.time()

        for idx, question_data in enumerate(questions, 1): # run on index and the questions data one by one
            print(f"Question {idx}: {question_data['question']}")
            options = question_data['incorrect_answers'] + [question_data['correct_answer']] # getting the questions answers right or wrong.
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")
            
            answer = True
            while answer is True:
                try:
                    user_answer = input("Your answer (1, 2, 3, 4): ")
                    convert = int(user_answer)
                    if convert > 4:
                        print("You must enter a number from 1-4")
                    else:
                        answer = False
                except ValueError:
                    print("Please enter digit and not a string")

            correct_answer_index = options.index(question_data['correct_answer']) + 1
            if user_answer == str(correct_answer_index):
                print("Correct!")
                correct_answers += 1
            else:
                print(f"Wrong! The correct answer is: {correct_answer_index}")

        print(f"\nHey {self.current_player}, you got {correct_answers} out of {total_questions} questions correct.")
        end_time = time.time()
        game_duration = end_time - start_time
        print(f'Game duration: {game_duration:.2f} seconds')

        return False    
    
    def questions(self, question_dict: dict):
        correct_answers = 0
        total_questions = len(question_dict)
        start_time = time.time()
        for question, data in question_dict.items():
            print(f"Question: {question}")
            for option, answer_text in data["options"].items():
                print(f"● {option}) {answer_text}")
            
            user_answer = input("Your answer: ")
            correct_answer = data["answer"]
            if user_answer.upper() == correct_answer.upper():
                print("Correct!")
                correct_answers += 1
            else:
                print(f"Wrong! The correct answer is: {correct_answer}")
        
        print(f"\nHey {self.current_player} You got {correct_answers} out of {total_questions} questions correct.")
        end_time = time.time()
        game_duration = end_time - start_time
        print(f'Game Duration was:' " {:.2f} seconds".format(game_duration))
        return False

    def start_game(self,level_of_game:str):
        """
        Starting the game.
        """
        game = True
        quizer.print_welcome()
        while game is True:
            ask = quizer.questions_from_api(difficulty=level_of_game)
            if ask is False:
                new_or_exit = True
                while new_or_exit is True:
                    new_game = input("""
    Do you want to start a [N]ew game or [E]xit ?
    """).lower()
                    if new_game == 'n':
                        print("Starting a new game! ")
                        new_or_exit - False
                        break
                    elif new_game == 'e':
                        print("Exiting the game! ")
                        new_or_exit - False
                        return
                    else:
                        print("Please enter N for new game or E to exit")
                        
name = input("Please enter your name: ")

while True:
    level_of_game = input("""Please enter difficulty: 
1.Easy
2.Medium
3.Hard
""").lower()
    
    print('level_of_game',level_of_game)
    if level_of_game == '1':
        print("Adjust the level of game to Easy mode.")
        level_of_game = 'easy'
        break
    elif level_of_game == '2':
        print("Adjust the level of game to Medium mode.")
        level_of_game = 'medium'
        break
    elif level_of_game == '3':
        print("Adjust the level of game to Hard mode.")
        level_of_game = 'hard'
        break
    else:
        print("Please choose the difficulty level by pressing number from 1-3")

quizer = Quiz(name)
quizer.start_game(level_of_game)