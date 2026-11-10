# Write a progam to read the text from a given file 'poem.txt' and fidn out whether it contains the word 'twinkle'.

with open("CHAPTER 9/PRACTICE SET/poem.txt", "r") as f:
    content = f.read()
    if "twinkle" in content:
        print("The word 'twinkle' is present in the file.") 
    else:
        print("The word 'twinkle' is not present in the file.")
