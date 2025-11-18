import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download required NLTK packages (run once)
# nltk.download('punkt')
# nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

text = input("Enter a sentence: ")

# Tokenize the sentence
words = word_tokenize(text)

print("\nLemmatized Words:")
for word in words:
    lemma = lemmatizer.lemmatize(word)
    print(f"{word} --> {lemma}")
