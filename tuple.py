#Task number 1
thistuple = (10,2.9,"Ahmed")

#Task number 2
integer,floate,stringe = thistuple
print(integer,floate,stringe)

#Task number 3
thistuple = (10,11,12,13,14,15,16,17,18,19,20)
print(thistuple[-4])

#Task number 4
if 10 in thistuple:
    print("Yes the given element exists")
else:
    print("The given element does not exist")

#Task number 5
thislist = [1,2,3,4,5,6,7,8,9,10]
thistuple = tuple(thislist)

#Task number 6
req_element = 10
req_index = thistuple.index(req_element)
print(req_index)