#Task 10
'''Here our client provides us with a list of students of each class and wants us to write a program to
identify if any of the students are studying multiple courses or not'''
list_of_medical_students = {"Ahmed","Haris","Afnan","Ehtesham"}
list_of_engineering_students = {"Abdullah","Mudassir","Ahmed","Taimoor","Ehtesham"}
list_of_computer_students = {"Usman","Inam","Imran","Ahmed","Ehtesham"}

extra_class_students = list_of_medical_students.intersection(list_of_engineering_students,list_of_computer_students)

if len(extra_class_students) > 0:
    print("The student(s) taking 1+ courses is/are: \n",extra_class_students)
else:
    print("None of the students are taking extra courses")