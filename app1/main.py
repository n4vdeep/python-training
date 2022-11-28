while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, edit, or complete. To see your Todos type show, or exit to close app: ")
    user_action = user_action.strip()

    # Match compares the user input to case
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # new_todos = []
            # for item in todos:
            #     new_item = item.strip("\n")
            #     new_todos.append(new_item)

            # List Comprehension
            # new_todos = [item.strip("\n") for item in todos]

            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Enter the number of the item you want to edit: "))
            number -= 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_item = input("Enter the item you want: ")
            todos[number] = new_item + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            completed_todo = int(input("Enter the number of the item you want to complete: "))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            index = completed_todo - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo item: '{todo_to_remove}' has been removed from the list"
            print(message)

        case 'exit':
            break
