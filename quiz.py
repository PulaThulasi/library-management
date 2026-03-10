# Quiz Application using list and loop

questions = [
    "1. What does CPU stand for?",
    "2. Which language is used for web development?",
    "3. Who developed Python?"
]

options = [
    ["A. Central Processing Unit", "B. Computer Personal Unit", "C. Central Program Unit"],
    ["A. HTML", "B. Python", "C. Both A and B"],
    ["A. James Gosling", "B. Guido van Rossum", "C. Dennis Ritchie"]
]

answers = ["A", "C", "B"]

score = 0

print("Welcome to the Python Quiz\n")

for i in range(len(questions)):
    print(questions[i])
    
    for option in options[i]:
        print(option)
        
    user_answer = input("Enter your answer (A/B/C): ")
    
    if user_answer.upper() == answers[i]:
        print("Correct!\n")
        score += 1
    else:
        print("Wrong answer\n")

print("Quiz Completed!")
print("Your Score:", score, "/", len(questions))