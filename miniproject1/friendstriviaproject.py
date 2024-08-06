#!/usr/bin/env python3
""" 'Friends' show trivia"""

import random

friends_trivia_questions = {
    "What is Monica's biggest pet peeve?": {
        "Choices": ["A. Animals dressed as humans", "B. People chewing with their mouths open", "C. Loud chewing noises", "D. Leaving the toilet seat up"],
        "Answer": "A"
    },
    "According to Chandler, what phenomenon scares the bejeezus out of him?": {
        "Choices": ["A. Big dogs", "B. The microwave", "C. Michael Flatley, Lord of the Dance", "D. Snakes"],
        "Answer": "C"
    },
    "Every week, the TV Guide comes to Chandler and Joey's apartment. What name appears on the address label?": {
        "Choices": ["A. Chandler Bing", "B. Chandler Bang", "C. Chanandler Bong", "D. Joey Tribbiani"],
        "Answer": "C"
    },
    "Rachel claims this is her favorite movie...": {
        "Choices": ["A. Dangerous Liaisons", "B. Titanic", "C. Gone with the Wind", "D. Weekend at Bernie's"],
        "Answer": "A"
    },
    "Rachel's actual favorite movie is?": {
        "Choices": ["A. Die Hard", "B. Weekend at Bernie's", "C. Titanic", "D. Dangerous Liaisons"],
        "Answer": "B"
    },
    "In what part of her body did Monica get a pencil stuck at age 14?": {
        "Choices": ["A. Ear", "B. Nose", "C. Hand", "D. Shoulder"],
        "Answer": "B"
    },
    "The next door neighbor, Mr. Heckles, was known for this...": {
        "Choices": ["A. Complaining", "B. Stealing newspaper", "C. Playing loud music", "D. Banging on the ceiling"],
        "Answer": "D"
    },
    "What is Chandler's job?": {
        "Choices": ["A. Transponster", "B. Statistical analysis and data reconfiguration", "C. Accountant", "D. Computer programmer"],
        "Answer": "B"
    },
    "What is Joey's favorite food?": {
        "Choices": ["A. Pizza", "B. Burgers", "C. Sandwiches", "D. Pasta"],
        "Answer": "C"
    }
}

#setting up the allowed number of guesses and the guess count
max_guesses = 3
guess_count = 0;

#Choosing a random number
trivia_question_number = random.randint(1,9)

#Function for getting a randomized trivia questoin 
def get_trivia_question(trivia_question_number):
    count = 1;
    for key,value in friends_trivia_questions.items():
        if count == trivia_question_number:
            return key
            break
        else: 
            count = count + 1
        
#getting the randomized trivia question/choices/answer
trivia_key = get_trivia_question(trivia_question_number)
choices = friends_trivia_questions[trivia_key]["Choices"]
answer = friends_trivia_questions[trivia_key]["Answer"]

#initial print of Game Title + Question
print("-----------FRIENDS (the tv show) Trivia Game---------------")
print(f"TRIVIA QUESTION:{trivia_key}")


while True:
    #Displaying choices
    print(f"CHOICES: {choices}")
    
    #User runs out of choices
    if guess_count == max_guesses:
        print(f"You have run out of guesses! The answer was : {answer}.")
        break
    
    #User input + checking if valid choice
    user_input = input(f"Choose a choice from above (A, B, C, or D): \nAttempt {guess_count + 1} of {max_guesses}>").upper().strip()
    if user_input not in["A","B","C","D"]:
        print("That is not a valid choice! Try Again! Please select A, B, C, or D.")
        print("-----------------------------------------------------------")
        continue
        
    #code block that checks wether right or wrong answer     
    if user_input == answer: 
        print("That is the correct answer! WOO!")
        break
    else:
        print("That is an incorrect answer! Try Again!")
        print("-----------------------------------------------------------")
        guess_count = guess_count + 1
   
    
    
    
    


