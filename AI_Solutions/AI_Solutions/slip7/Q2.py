print("Simple AI Chatbot\n")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "bye":
        print("Bot: Goodbye!")
        break

    elif "hello" in user or "hi" in user:
        print("Bot: Hello! How can I help you?")

    elif "name" in user:
        print("Bot: I am a simple AI chatbot created in Python.")

    elif "college" in user:
        print("Bot: You are studying at SP Pune University.")

    elif "course" in user:
        print("Bot: This is the Artificial Intelligence Practical course.")

    else:
        print("Bot: Sorry, I don't understand that.")
