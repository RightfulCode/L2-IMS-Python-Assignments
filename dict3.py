#Task 9
'''In this program, we use nested dictionaries to store data about different students and their marks in
each subject. we can input the name of any student and we will be shown the marks that student gained in
total and in each subject.'''
data_dict = {
    "Maths":{
        "Ali":89,
        "Burhan":78,
        "Mudassir":92
    },
    "Physics":{
        "Ali":70,
        "Burhan":100,
        "Mudassir":55
    },
    "Computer Science":{
        "Ali":100,
        "Burhan":40,
        "Mudassir":98
    },
    "Biology":{
        "Ali":38,
        "Burhan":67,
        "Mudassir":100
    }
}
def mathmarks(x):
    return data_dict["Maths"][x]

def physicmarks(x):
    return data_dict["Physics"][x]

def compmarks(x):
    return data_dict["Computer Science"][x]

def biomarks(x):
    return data_dict["Biology"][x]

name = input("Please enter the name of the student you would like to view the marks of: \n").lower()
name = name.capitalize()

if name in data_dict["Maths"]:
    maths = mathmarks(name)
    physics = physicmarks(name)
    computer = compmarks(name)
    bio = biomarks(name)

    total = 400
    marks_obtained = maths + physics + computer + bio
    percentage = round(marks_obtained/4,1)
    print(f'''out of 400 marks,{name} achived {marks_obtained} marks with a percentage of {percentage}%
    {maths} marks in maths
    {physics} marks in physics
    {computer} marks in computer science
    {bio} marks in biology''')
else:
    print("Student does not exist")