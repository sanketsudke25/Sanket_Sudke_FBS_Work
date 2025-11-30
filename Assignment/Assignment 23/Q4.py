quiz = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
        "answer": "A"
    },
    {
        "question": "Which language is primarily used for web development?",
        "options": ["A. Python", "B. JavaScript", "C. C++", "D. Java"],
        "answer": "B"
    },
    {
        "question": "What is 5 * 6?",
        "options": ["A. 11", "B. 30", "C. 56", "D. 25"],
        "answer": "B"
    },
    {
        "question": "Who developed the theory of relativity?",
        "options": ["A. Isaac Newton", "B. Albert Einstein", "C. Galileo Galilei", "D. Nikola Tesla"],
        "answer": "B"
    }
]

def quiz_game():
    print("=== Welcome to the Quiz Game ===")
    score = 0
    for q in quiz:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        user_answer = input("Enter your answer (A/B/C/D): ").upper()
        if user_answer == q["answer"]:
            print(" Correct!")
            score += 1
        else:
            print(f" Incorrect! The correct answer is {q['answer']}.")

    print("\n=== Quiz Finished ===")
    print(f"Your final score: {score}/{len(quiz)}")
quiz_game()