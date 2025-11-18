sentence = input("Enter a sentence: ")

words = sentence.split()
words.sort()

print("Sorted Sentence:")
print(" ".join(words))
