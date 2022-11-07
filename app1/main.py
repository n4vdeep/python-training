user_prompt = "Enter a ToDo item: "

todos = []
while True:
    todo = input(user_prompt)
    upper = todo.upper()
    todos.append(upper)
    print(todos)
