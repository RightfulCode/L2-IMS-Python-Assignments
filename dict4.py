#Task 10
dict_data = {}

loop = 0
while loop == 0:
    action = input("type 'help' to view the list of commands \n").lower()
    if "add" in action:
        key = input("Enter the key to be added: \n")
        value = input("Assign a value to the key you just created: \n")
        dict_data[key] = value
    elif "remove" in action:
        if len(dict_data) == 0:
            print("Error, no items exist in the dictionary")
        else:
            print(dict_data)
            remove = input("Enter the item to be removed using its key: \n")
            dict_data.pop(remove)
    elif "final" in action:
        print(dict_data)
        loop += 1
    elif "help" in action:
        print('''The commands are:
        1: add
        2: remove
        3: final
        4: exit''')
    elif "exit" in action:
        loop += 1
    else:
        print("Invalid command")