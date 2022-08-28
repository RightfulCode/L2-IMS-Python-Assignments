student_dict = {}

def dict_add(student_name,student_list):
    n = 0
    for x in student_list:
        n += x
    student_dict[student_name] = n

def marks():
    physics = float(input("Enter marks attained in physics: \n"))
    chemistry = float(input("Enter marks attained in chemistry: \n"))
    math = float(input("Enter marks attained in maths: \n"))
    return [physics,chemistry,math]

def get_position(stud1,stud2,stud3,stud4,stud5):
    all_marks = [stud1,stud2,stud3,stud4,stud5]
    all_marks.sort(reverse=True)
    key_list = list(student_dict.keys())
    value_list = list(student_dict.values())
    first,second,third = value_list.index(all_marks[0]),value_list.index(all_marks[1],1),value_list.index(all_marks[2],2)
    first_position,second_position,third_position = key_list[first],key_list[second],key_list[third]
    return [first_position,second_position,third_position]

print("Current student: Zeeshan, Roll no: 0")
zeeshan_subject_marks = marks()
dict_add("Zeeshan",zeeshan_subject_marks)

print("Current student: Umair, Roll no: 1")
umair_subject_marks = marks()
dict_add("Umair",umair_subject_marks)

print("Current student: Imran, Roll no: 2")
imran_subject_marks = marks()
dict_add("Imran",imran_subject_marks)

print("Current student: Waleed, Roll no: 3")
waleed_subject_marks = marks()
dict_add("Waleed",waleed_subject_marks)

print("Current student: Arsalan, Roll no: 4")
arsalan_subject_marks = marks()
dict_add("Arsalan",arsalan_subject_marks)

position = get_position(student_dict["Zeeshan"],student_dict["Umair"],student_dict["Imran"],student_dict["Waleed"],student_dict["Arsalan"])
student_list = list(student_dict)
print(f'''First Position:{position[0]} Roll no:{student_list.index(position[0])} who achieved {student_dict.get(position[0])} marks out of 300
Second Position:{position[1]} Roll no:{student_list.index(position[1])} who achieved {student_dict.get(position[1])} marks out of 300
Third Position:{position[2]} Roll no:{student_list.index(position[2])} who achieved {student_dict.get(position[2])} marks out of 300''')