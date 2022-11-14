filenames = ['document', 'report', 'presentation']
ips = ['100.122.133.105', '100.122.133.111']

for index, item in enumerate(filenames):
    print(f"{index}-{item.capitalize()}.txt")

user_action = int(input("Enter the index of the IP you want: "))
user_action -= 1
print(f"You chose {ips[user_action]}")

