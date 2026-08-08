"""
CodeAlpha - Python Programming Internship
Task 4: Basic Chatbot

A simple rule-based chatbot that responds to a fixed set of greetings
and phrases using if-elif logic.
"""

import random

RESPONSES = {
    "hello": ["Hi!", "Hello there!", "Hey! How can I help you today?"],
    "hi": ["Hi!", "Hello!", "Hey there!"],
    "how are you": ["I'm fine, thanks!", "Doing great, thanks for asking!"],
    "what is your name": ["I'm a simple rule-based chatbot built for CodeAlpha.", "You can call me CodeBot!"],
    "help": ["I can chat about greetings and basic small talk. Try saying 'hello' or 'how are you'."],
    "thank you": ["You're welcome!", "Anytime!"],
    "thanks": ["You're welcome!", "No problem!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Take care!"],
    "goodbye": ["Goodbye!", "Bye! Take care!"],
}

EXIT_WORDS = {"bye", "goodbye"}


def get_response(user_input):
    """Return a chatbot reply based on simple keyword matching."""
    text = user_input.lower().strip()

    for keyword, replies in RESPONSES.items():
        if keyword in text:
            return random.choice(replies), keyword in EXIT_WORDS

    return "Sorry, I didn't understand that. Type 'help' to see what I can do.", False


def chat():
    print("=== Basic Chatbot ===")
    print("Type 'bye' or 'goodbye' to end the conversation.\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("Bot: Please type something.")
            continue

        reply, should_exit = get_response(user_input)
        print(f"Bot: {reply}")

        if should_exit:
            break


if __name__ == "__main__":
    chat()
