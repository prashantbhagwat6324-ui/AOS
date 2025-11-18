print("Simple AI Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "bye":
        print("Bot: Goodbye!")
        break

    elif "hi" in user or "hello" in user:
        print("Bot: Hello! How can I help you?")

    elif "name" in user:
        print("Bot: I am a Python Chatbot created for AI practicals.")

    elif "college" in user:
        print("Bot: You are studying at Savitribai Phule Pune University.")

    elif "course" in user:
        print("Bot: This is the Artificial Intelligence lab course.")

    else:
        print("Bot: Sorry, I didn't understand that.")
