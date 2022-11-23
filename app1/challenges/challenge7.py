names = ["john smith", "jay santi", "eva kuki"]
names = [name.title() for name in names]
print(names)


usernames = ["john 1990", "alberta1970", "magnola2000"]
usernames_char_len = [len(user) for user in usernames]
print(usernames_char_len)

user_entries = ['10', '19.1', '20']
user_entries = [float(number) for number in user_entries]
print(user_entries)

user_entries = ['10', '19.1', '20']
user_entries = [float(i) for i in user_entries]
sum_of_user_entries = sum(user_entries)
print(sum_of_user_entries)
