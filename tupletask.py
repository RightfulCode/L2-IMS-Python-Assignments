#Task 7
'''Here our client is asking us to develop an app used for the convenience of its customers.
We have to develop an app which keeps track of the list of items of the user.'''

item_tuple = ()

intro = 0
while intro == 0:
    question = input("Type 'help' to view the list of commands \n")
    if "Add" in question or "add" in question:
        item_list = list(item_tuple)
        action = input("Please enter the item to be added: \n")
        item_list.append(action)
        item_tuple = tuple(item_list)
    elif "Remove" in question or "remove" in question:
        print(item_tuple)
        item_list = list(item_tuple)
        action = input("Please enter the item to be removed: \n")
        item_list.remove(action)
        item_tuple = tuple(item_list)
    elif "Final" in question or "final" in question:
        print(item_tuple)
        intro += 1
    elif "Exit" in question or "exit" in question:
        intro += 1
    elif "Help" in question or "help" in question:
        print('''The commands are as follows:
        1: (A/a)dd (to add an item)
        2: (R/r)emove (to remove an item)
        3: (F/f)inal (to get the complete list)
        4: (E/e)xit (to exit the program)''')