import json

questions_answers = {
    "q1": {
        "question": "What is the capital of France?",
        "answers": "Paris"
    },
    "q2": {
        "question": "What is the largest planet in our solar system?",
        "answers": "Jupiter"
        
    },
    "q3": {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "answers": "Harper Lee"
    },
    "q4": {
        "question": "What is the chemical symbol for gold?",
        "answers": "Au"
    },
    "q5": {
        "question": "Who painted the Mona Lisa?",
        "answers": "Leonardo da Vinci"
    }

}
with open ("questions.json", "w" ) as f:
    json.dump(questions_answers, f, indent=4)
with open("questions.json", "r") as f:
    data = json.load(f)
    score = 0
    for question in questions_answers:
        user_answer = input(questions_answers[question]["question"] + " ")
        if user_answer.lower() == questions_answers[question]["answers"].lower():
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
print(f"Your final score is {score}/ {len(questions_answers)}")
    