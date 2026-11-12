# Write a program to update a file by replacing "Donkey" with ###

def remove():
    with open("PRACTICE SET/04.txt", "r") as file:
        data = file.read()
        data = data.replace("Donkey", "###")
    with open("PRACTICE SET/04.txt", "w") as file:
        file.write(data)

remove() 
