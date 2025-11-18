import random

words = ["python", "hangman", "programming", "computer", "artificial"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
used_letters = []

print("Welcome to Hangman!")
print("Word:", " ".join(guessed))

while attempts > 0:
    guess = input("Enter a letter: ").lower()

    if guess in used_letters:
        print("You already used this letter!")
        continue

    used_letters.append(guess)

    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

    print("Word:", " ".join(guessed))

    if "_" not in guessed:
        print("You won! The word was:", word)
        break

if attempts == 0:
    print("You lost! The word was:", word)
