import time
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
You will be presented with multiple-choice questions. Enter the letter
corresponding to your answer.

""")
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

    def start_game(self):
        """
        Starting the game.
        """
        game = True
        quizer.print_welcome()
        while game is True:
            ask = quizer.questions(all_questions)
            if ask is False:
                new_exit = True
                while new_exit is True:
                    new_game = input("""
    Do you want to start a [N]ew game or [E]xit ?
    """).lower()
                    if new_game == 'n':
                        print("Starting a new game! ")
                        new_exit - False
                        break
                    elif new_game == 'e':
                        print("Exiting the game! ")
                        new_exit - False
                        return
                    else:
                        print("Please enter N for new game or E to exit")
                        


  

name = input("Please enter your name: ")
quizer = Quiz(name)
quizer.start_game()