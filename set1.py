#Task 7
'''The following is another app that keeps track of items and stores them in set. This one is better
modified and uses sets instead of a tuple.'''
set_of_items = set({})
loop = 0

while loop == 0:
    action = input("type 'help' to see the list of commands \n").lower()

    if "add" in action:
        add_item = input("Enter the item to be added: \n").lower()
        if add_item in set_of_items:
            print("Item already exists in the list")
        else:
            set_of_items.add(add_item)
            print("Added, The current list is: \n ",set_of_items)
    elif "remove" in action:
        if len(set_of_items) == 0:
            print("Error, no items present to be removed")
        else:
            print(set_of_items)
            remove_item = input("Enter the item to be removed: \n").lower()
            if remove_item not in set_of_items:
                print("Specified item does not exist")
            else:
                set_of_items.remove(remove_item)
                if len(set_of_items) == 0:
                    print("Removed, the current list is empty")
                else:
                    print("Removed, the current list is: \n",set_of_items)
    elif "final" in action:
        if len(set_of_items) == 0:
            print("The list is empty")
            loop += 1
        else:
            print("The final list is: \n",set_of_items)
            loop += 1
    elif "help" in action:
        print('''The valid commands are:
        1: add
        2: remove
        3: final
        4: consecutive 
        5: exit''')
    elif "exit" in action:
        loop += 1
    elif "consecutive" in action:
        cons_add = int(input("Enter the amount of items to be added: \n"))
        for i in range(cons_add):
            add_item2 = input("Enter the item to be added: \n").lower()
            if add_item2 in set_of_items:
                print("Item already exists in the list")
            else:
                set_of_items.add(add_item2)
                print("Added, the current list is: \n",set_of_items)
    else:
        print("Please input a valid command")