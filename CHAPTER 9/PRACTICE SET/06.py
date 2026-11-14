with open("PRACTICE SET/log.txt","r") as file:
    content = file.read()

if "python" in content:
    print("Python is present in the log file.")
else:
    print("Python is not present in the log file.")
