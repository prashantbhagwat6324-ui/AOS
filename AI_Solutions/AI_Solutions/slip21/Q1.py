import string

text = input("Enter a string: ")

punctuations = string.punctuation

cleaned = ""
for char in text:
    if char not in punctuations:
        cleaned += char

print("Original String:", text)
print("String After Removing Punctuations:", cleaned)
