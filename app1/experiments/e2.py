# The infinite loop
while True:
    print("Hello Pypy")

# Readable syntax
todos = []
while True:
    # is having the variable better inside the loop?
    user_prompt = "Enter a ToDo item: "
    todo = input(user_prompt)
    upper = todo.upper()
    todos.append(upper)
    print(todos)

# Use a different list method
user_prompt = "Enter a ToDo item: "

todos = []
while True:
    todo = input(user_prompt)
    upper = todo.title()
    todos.append(upper)
    print(todos)

# Remove method parenthesis
user_prompt = "Enter a ToDo item: "

todos = []
while True:
    todo = input(user_prompt)
    title = todo.title
    todos.append(title)
    print(todos)
