todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'edit':
            number = int(input("Enter the number of the item you want to edit: "))
            number -= 1
            new_item = input("Enter the item you want: ")
            todos[number] = new_item
        case 'exit':
            break
