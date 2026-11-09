# By using the "with" statement, we don't have to use the f.close() method.
with open("CHAPTER 9/file.txt", "r") as f:
    print(f.read())