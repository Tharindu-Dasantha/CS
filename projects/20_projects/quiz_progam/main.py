Quiz = {
    "Question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "Question2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "Question3": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "Question4": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "Question5": {
        "question": "What is the capital of Portugal?",
        "answer": "Lisbon"
    },
    "Question6": {
        "question": "What is the capital of Switzerland?",
        "answer": "Bern"
    },
    "Question7": {
        "question": "What is the capital of Austraia?",
        "answer": "Vienna"
    }
}

score = 0

for key, value in Quiz.items():
    print(value['question'])
    answer = input("Answer: ").title()
    if answer == value["answer"]:
        print("Correct")
        score += 1
    else:
        print("Wrong answer")
        print("Answer is "+ value['answer'])
        
print("Score: "+ str((score/7)*100) + '%')