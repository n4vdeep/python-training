file = open("../files/essay.txt", "r")
content = file.readline()
num_of_chars = len(content)

print(content.title())
print(num_of_chars)

user_action = input("Add a new member: ") + "\n"
file = open("../files/members.txt", "r")
new_member = file.readlines()
file.close()

new_member.append(user_action)

file = open("../files/members.txt", "w")
file.writelines(new_member)
file.close()

word = ["Hello", "Hello", "Hello"]
filenames = ["doc.txt", "report.txt", "presentation.txt"]

for word, filename in zip(word, filenames):
    file = open(f"../files/{filename}", "w")
    file.write(word)

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for filename in filenames:
    file = open(filename, "w")
    file.write("This is the actual solution")
    file.close()

filenames = ["../files/a.txt", "../files/b.txt", "../files/c.txt"]
for filename in filenames:
    file = open(filename, "r")
    output = file.readline()
    print(output)
    file.close()
