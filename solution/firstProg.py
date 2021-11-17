with open("file1.txt") as file1:
    text1 = file1.read();
    text2 = "".join(reversed(text1))

with open("file2.txt", "w") as file2:
    file2.write(text2)

with open("file1.txt") as file1:
    print(file1.read())

with open("file2.txt") as file2:
    print(file2.read())