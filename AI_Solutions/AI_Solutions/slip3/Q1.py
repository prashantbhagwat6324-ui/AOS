punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

text = input("Enter a string: ")
result = ""

for char in text:
    if char not in punctuations:
        result += char

print("String without punctuations:")
print(result)
