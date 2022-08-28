student_dict = {}

def dict_add(student_name,student_list):
    student_dict[student_name] = student_list
    total_marks = student_dict.get(student_name)
    n = 0
    for x in total_marks:
        n += x
    student_dict[student_name] = n
    return n

def marks():
    physics = int(input("Enter marks attained in physics: \n"))
    chemistry = int(input("Enter marks attained in chemistry: \n"))
    math = int(input("Enter marks attained in maths: \n"))
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
zeeshan_total_marks = dict_add("Zeeshan",zeeshan_subject_marks)

print("Current student: Umair, Roll no: 1")
umair_subject_marks = marks()
umair_total_marks = dict_add("Umair",umair_subject_marks)

print("Current student: Imran, Roll no: 2")
imran_subject_marks = marks()
imran_total_marks = dict_add("Imran",imran_subject_marks)

print("Current student: Waleed, Roll no: 3")
waleed_subject_marks = marks()
waleed_total_marks = dict_add("Waleed",waleed_subject_marks)

print("Current student: Arsalan, Roll no: 4")
arsalan_subject_marks = marks()
arsalan_total_marks = dict_add("Arsalan",arsalan_subject_marks)

position = get_position(zeeshan_total_marks,umair_total_marks,imran_total_marks,waleed_total_marks,arsalan_total_marks)
student_list = list(student_dict)
print(f'''First Position:{position[0]} Roll no:{student_list.index(position[0])}
Second Position:{position[1]} Roll no:{student_list.index(position[1])}
Third Position:{position[2]} Roll no: {student_list.index(position[2])}''')