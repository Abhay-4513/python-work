f = open("CHAPTER 9/file.txt", "r")

# lines = f.readlines()
# print(lines,type(lines))

# f.close()

line = f.readline()
while line != "":
    print(line)
    line = f.readline()
f.close()