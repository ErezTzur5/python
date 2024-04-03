import requests

url = 'https://opentdb.com/api.php?amount=10&category=27&difficulty=hard&type=multiple'
response = requests.get(url)
data = response.json()

questions = []
for result in data['results']:
    question = result['question']
    correct_answer = result['correct_answer']
    incorrect_answers = result['incorrect_answers']
    options = incorrect_answers + [correct_answer]
    questions.append({'question': question, 'options': options, 'answer': correct_answer})

for idx, question in enumerate(questions, 1):
    print(f"Question {idx}: {question['question']}")
    for i, option in enumerate(question['options'], 1):
        print(f"{i}. {option}")
    print(f"Correct Answer: {question['answer']}\n")
