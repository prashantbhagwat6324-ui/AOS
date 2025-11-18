import nltk
from nltk.corpus import stopwords

# Download once if not downloaded
# nltk.download('stopwords')

# Read passage from a text file
file_path = "input.txt"   # your file name
with open(file_path, "r") as f:
    text = f.read()

# Load English stopwords
stop_words = set(stopwords.words('english'))

# Split into words
words = text.split()

# Remove stopwords
filtered_words = [word for word in words if word.lower() not in stop_words]

print("Original Text:\n", text)
print("\nText After Removing Stopwords:\n")
print(" ".join(filtered_words))
