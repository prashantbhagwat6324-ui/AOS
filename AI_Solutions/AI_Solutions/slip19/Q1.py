import random

# List of words
words = ["python", "computer", "hangman", "science", "program"]

# Select random word
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
used_letters = []

print("Welcome to Hangman Game!")
print("Guess the word letter by letter.\n")

while attempts > 0:
    print("Word: ", " ".join(guessed))
    print(f"Attempts left: {attempts}")
    print("Used letters:", used_letters)

    letter = input("Enter a letter: ").lower()

    if letter in used_letters:
        print("You already used this letter!\n")
        continue

    used_letters.append(letter)

    if letter in word:
        print("Correct!\n")
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
    else:
        print("Wrong!\n")
        attempts -= 1

    if "_" not in guessed:
        print("Congratulations! You guessed the word:", word)
        break

if attempts == 0:
    print("You lost! The word was:", word)
