import random


# ----------------------------
# Rule-Based Chatbot Responses
# ----------------------------


responses = {
    "hello": ["Hello! How can I help you?", "Hi there!", "Hey! What's up?"],
    "hi": ["Hello!", "Hi! How can I assist you?", "Hey!"],
    "how are you": ["I'm doing great! Thanks for asking.", "Feeling awesome!", "I'm good! How can i help you?"],
    "name": ["I'm Chatbot created with python.", "You can call me Rulebot!"],
    "weather": ["I can't check live weather, but it's always sunny in python world"],
    "joke": [
        "why don't programmers like nature? Too many bugs!",
        "why did python live on the computer? Because it loved bytes!",
        "what do you call 8 hobbits? A hobbytes!"
    ],
    "thanks":["You're welcome!", "Happy to help!", "Anytime!"], 
    "bye": ["Goodbye!", "See you soon!", "Bye! Take care!"]
}


# -----------------------------
# Chatbot Function
# -----------------------------

def chatbot():
    print("Rule-Based Chatbot Started! (type 'bye' to exit)")

    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if user_input == "bye":
            print("Bot:", random.choice(responses["bye"]))
            break

        found = False

        #Rule Matching
        for key in responses:
            if key in user_input:
                print("Bot:", random.choice (responses[key]))
                found = True
                break

        # If no rule matched
        if not found:
            print("Bot: Sorry,I didn't understand that.")


# Run the chatbot
chatbot()
            
