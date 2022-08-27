#Task 8
'''The client is asking us to make a program which removes all the duplicates from a tuple of integers.
It should also sort the tuple in ascending order.'''
thistuple = (1,1,1,1,1,2,2,3,3,3,4,4,4,4,5,6,7,6,5,8,9,10)

for x in thistuple:
    if thistuple.count(x) > 1:
        thislist = list(thistuple)
        thislist.remove(x)
        thislist.sort()
        thistuple = tuple(thislist)
print(thistuple)