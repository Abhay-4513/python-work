# Repeat the program 4 for a list of such words to be censored.

censored_words = ["Donkey","Bad","Stupid",]

with open("PRACTICE SET/05.txt", "r") as file:
    data = file.read()

# Convert censored words to lowercase
censored_words = [word.lower() for word in censored_words]

# Convert file content to lowercase
data = data.lower()

for words in censored_words:
    data = data.replace(words, "###" * len(words))

with open("PRACTICE SET/05.txt", "w") as file:
    file.write(data)
