import random
import sys

greetings = ['hola', 'hello', 'hi', 'konnichiwa', 'hey!', 'hey', 'heyo', "'sup", "ni hao",'yo']
random_greeting = random.choice(greetings)

question = ['how are you?', 'how are you doing?', "how you doing?"]
responses = ['Okay. How are you?', "I'm fine. How are you today?", "Good, you?"]
random_response = random.choice(responses)

response = ['fine', 'good', 'bad', "i've been better", 'okay']
questions = ["Can you tell me one of your hobbies?", "What is your favorite game?"]
random_questions= random.choice(questions)

endings = ['goodbye', 'bye', 'bai bai', 'ciao', 'sayonara', 'jai jian', 'see ya', 'ok bye']
random_endings = random.choice(endings)

while True:
    userInput = input(">>> ").lower()
    if userInput in greetings:
        print(random_greeting)
    elif userInput in question:
        print(random_response)
    elif userInput in response:
        print(random_questions)
        answer = input(">>> ")
        print("Really?", str.capitalize(answer) + " sounds so cool! I should try that someday!")
    elif userInput in endings:
        print(random_endings)
        sys.exit()
    else:
        print("I did not understand what you said.")
