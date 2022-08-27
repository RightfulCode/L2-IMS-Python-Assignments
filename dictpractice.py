#Task 1
thisdict = {
    "Ali":75,
    "Ahmad":66,
    "Hamza":45,
    "Zahid":89,
    "Junaid":33
}

#Task 2
print(thisdict["Hamza"])

#Task 3
thisdict["Ahmad"] = 88
print(thisdict["Ahmad"])

#Task 4
thisdict.pop("Hamza")
print(thisdict)

#Task 5
thislist = [x for x in thisdict]
thislist.sort()
print(thislist)

#Task 6
mathdict = thisdict.copy()
mathdict["Junaid"] = 55
print(mathdict)