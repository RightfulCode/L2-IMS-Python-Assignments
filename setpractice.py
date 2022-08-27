#Task 1
fruits = {"apple","banana","cherry"}
fruits.add("orange")
print(fruits)

#Task 2
fruits = {"apple","banana","cherry"}
more_fruits = ["orange","mango","grapes"]
fruits.update(more_fruits)
print(fruits)

#Task 3
fruits = {"apple","banana","cherry"}
fruits.remove("banana")
print(fruits)

#Task 4
x = {22,34,55}
y = {34,25,54}
z = list(x.symmetric_difference(y))
print(z)

#Task 5
set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}
set3 = set1.intersection(set2)
print(set3)

#Task 6
set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}
set3 = set1.intersection(set2)
if len(set3) > 0:
    print(set3)