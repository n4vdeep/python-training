# Default mode is r
with open("../files/doc.txt", "r") as file:
    output = file.read()
    print(output)
