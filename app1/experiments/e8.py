# # Default mode is r
# with open("../files/doc.txt", "r") as file:
#     output = file.read()
#     print(output)


with open("../files/test_file.txt", 'r') as file:
    output = file.read()
    print(output)
    print(len(output))
