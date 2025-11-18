def chatbot():
    print("Chatbot: Hello! I am your simple chatbot.")
    print("Type 'bye' to exit.\n")

    responses = {
        "hi": "Hello! How can I help you?",
        "hello": "Hi there! What’s up?",
        "name": "My name is SimpleBot.",
        "college": "Your college is XYZ College.",
        "course": "You are studying B.Sc Computer Science.",
        "fees": "Please check the office for fee details.",
        "exam": "Exams will be announced soon."
    }

    while True:
        user = input("You: ").lower()

        if user == "bye":
            print("Chatbot: Goodbye!")
            break

        matched = False
        for keyword in responses:
            if keyword in user:
                print("Chatbot:", responses[keyword])
                matched = True
                break

        if not matched:
            print("Chatbot: I don't understand that. Try another question.")

chatbot()
