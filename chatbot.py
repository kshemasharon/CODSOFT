import random

def respond_to_greeting(user_input):
    greetings = ['hello', 'hi', 'hey', 'howdy']
    bot_greetings = ['Hello!', 'Hi!', 'Hey!', 'Howdy!']
    response = random.choice(bot_greetings)
    return response

def respond_to_question(user_input):
    questions = ['how are you', 'what is your name', 'who are you','What is the weather like today?','How can i help you?']
    bot_responses = {
        'how are you': ['I am good, thanks!', 'I\'m doing well, how about you?'],
        'what is your name': ['I am a simple chatbot.', 'You can call me Chatbot.'],
        'who are you': ['I am a virtual assistant designed to help with simple tasks.'],
        'how can i help you':['I can help you to solve simple tasks.']
    }
    for pattern, responses in bot_responses.items():
        if pattern in user_input:
            return random.choice(responses)
    return "I'm not sure how to respond to that."

def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if any(greeting in user_input for greeting in ['hello', 'hi', 'hey']):
        return respond_to_greeting(user_input)
    elif any(question in user_input for question in ['how are you', 'what is your name', 'who are you']):
        return respond_to_question(user_input)
    else:
        return "I'm not sure how to respond to that."

# Example usage:
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    else:
        response = chatbot_response(user_input)
        print("Chatbot:", response)



