def college_bot():
    info = {
        "name": "Sachin Pukale",
        "course": "B.Sc. Computer Science",
        "year": "Final Year",
        "rollno": "32",
        "college": "Your College Name",
        "department": "Computer Science Department",
        "hod": "Dr. XYZ",
        "class teacher": "Prof. ABC",
        "fees": "Check office for fee details.",
        "library": "Library timing: 9 AM to 5 PM",
        "exam": "Exam timetable will be announced soon."
    }

    print("Welcome to the College Information Bot!")
    print("Ask anything related to your college details.")
    print("Type 'exit' to stop.\n")

    while True:
        user = input("You: ").lower()

        if user == "exit":
            print("Bot: Goodbye!")
            break

        matched = False
        for key in info:
            if key in user:
                print("Bot:", info[key])
                matched = True
                break

        if not matched:
            print("Bot: Sorry, I don't have that information.")

college_bot()
