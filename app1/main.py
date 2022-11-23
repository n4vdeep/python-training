while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, edit, or complete. To see your Todos type show, or exit to close app: ")
    user_action = user_action.strip()

    # Match compares the user input to case
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

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
            new_item = input("Enter the item you want: ")
            todos[number] = new_item
        case 'complete':
            completed_todo = int(input("Enter the number of the item you want to complete: "))
            completed_todo -= 1
            todos.pop(completed_todo)
        case 'exit':
            break
