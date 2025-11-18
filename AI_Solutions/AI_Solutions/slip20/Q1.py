def college_bot():
    info = {
        "name": "Sachin Pukale",
        "course": "B.Sc. Computer Science",
        "year": "Final Year",
        "div": "A",
        "rollno": "32",
        "college": "Your College Name",
        "department": "Computer Science Department",
        "hod": "Dr. XYZ",
        "class_teacher": "Prof. ABC",
        "fees": "All fees details available in office",
        "exam": "Exam dates will be announced on notice board",
        "library": "Library is open from 9 AM to 5 PM"
    }

    print("Welcome to College Info Bot!")
    print("Ask anything related to your college details.")
    print("Type 'exit' to stop.\n")

    while True:
        user = input("You: ").lower()

        if user == "exit":
            print("Bot: Thank you! Have a good day.")
            break

        found = False
        for key in info:
            if key in user:
                print("Bot:", info[key])
                found = True
                break

        if not found:
            print("Bot: Sorry, I don't have information about that.\n")

college_bot()
