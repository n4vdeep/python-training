while True:
    user_action = input("Enter country you are from? or End to exit program: ")
    user_action = user_action.lower()

    match user_action:
        case 'usa':
            print("Hello")
        case 'india':
            print("Namaste")
        case 'germany':
            print("Halo")
        case 'end':
            break

ingredients = ["john smith", "sen plakay", "dora ngacely"]
for ingredient in ingredients:
    print(ingredient.title())