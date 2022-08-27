#Task 9
'''Here, the client gives us information in the form of a tuple in which the first element is the amount
of orders, the rest of the elements are all the individual parts price for the orders specified.
The client wants us to find the total cost and price of each part on any amounts of order and return the
information in the form of a tuple'''

thistuple = (4,50,500,100,1000,200)

no_of_orders,*parts_cost = thistuple

total_cost = 0
for i in parts_cost:
    total_cost += i
total_cost_per_order = total_cost/4
part1_cost = thistuple[1]/4
part2_cost = thistuple[2]/4
part3_cost = thistuple[3]/4
part4_cost = thistuple[4]/4
part5_cost = thistuple[5]/4
orders = int(input("Please enter the amount of orders: \n"))
total_specified_cost = round(total_cost_per_order * orders)
part1_specified_cost = round(part1_cost * orders)
part2_specified_cost = round(part2_cost * orders)
part3_specified_cost = round(part3_cost * orders)
part4_specified_cost = round(part4_cost * orders)
part5_specified_cost = round(part5_cost * orders)

newtuple = (orders,total_specified_cost,part1_specified_cost,part2_specified_cost,part3_specified_cost,part4_specified_cost,part5_specified_cost)
print(newtuple)