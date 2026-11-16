with open("PRACTICE SET/log.txt", "r") as file:
    lines = file.readlines()

lineno = 1
for line in lines:
    if"python" in line.lower():
        print(f"Yes python is present in line no : {lineno}")
    lineno += 1

else:
    print("No python is present in the file")
