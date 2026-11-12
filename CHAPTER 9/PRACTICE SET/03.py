# Write a python program to create a multiplication table of numbers from 2 to 20 and save them in a folder named "multiplication-folder" with the name of the file as "table_n.txt" where n is the number for which the table is created.

def table(n):
    a = ""
    for i in range(1,11):
        a += f"{n} X {i} = {n*i}\n"

    # Open the file in append mode
    f = open(f"PRACTICE SET/multiplication-folder/table_{n}.txt", "w")
    f.write(a)
    f.close()

for i in range(2,21):
    table(i)
