import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Read passage from file
with open("input.txt", "r") as file:
    text = file.read()

# Tokenize
words = word_tokenize(text)

# Load English stopwords
stop_words = set(stopwords.words("english"))

# Remove stopwords
filtered_words = [w for w in words if w.lower() not in stop_words]

print("Original Text:")
print(text)

print("\nFiltered Text:")
print(" ".join(filtered_words))
