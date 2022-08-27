#Task number 1
thislist = [x for x in range(1,1001)]

#Task number 2
newlist = [x for x in thislist if x%17 == 0]

#Task number 3
newlist_length = len(newlist)
print(f"The amount of integers divisible by 17 are {newlist_length}.")

#Task number 4
even_num_list = [x for x in newlist if x%2 == 0]
odd_num_list = [x for x in newlist if x%2 != 0]
print(even_num_list)
print(odd_num_list)

#Task number 5
even_num_length = len(even_num_list)
odd_num_length = len(odd_num_list)
print(f'''The amount of even numbers are {even_num_length}. 
The amount of odd numbers are {odd_num_length}.''')