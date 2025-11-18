sentence = input("Enter a sentence: ")

words = sentence.split()

words.sort()

print("Sorted Sentence:")
for w in words:
    print(w, end=" ")
