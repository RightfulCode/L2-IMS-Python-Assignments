#Task 7
'''Here, our client has requested us to create a program that can access the data of a patient by just
typing in their name. Here the patient info is already provided and all we have to do is print it out
repectively and in on organized form'''
patient_history = {
    "Ahmad":["18th July,2020","20th February,2021","Aspirin,Ibuprofen,Naproxen"],
    "Usman":["28th January,2021","Still admit","Paracetamol,Aspirin"],
    "Ali":["2nd June,2022","1st July,2022","Albuterol,Morphine"]
}

def get_history(x):
    return patient_history.get(x)

def description(x):
    if x[1] != "Still admit":
        print(f'''Patient was admitted on {x[0]}
The patient left on {x[1]}
The medicine they took were {x[2]}''')
    else:
        print(f'''Patient was admitted on {x[0]}
The patient is still admitted
The medicine they are currently taking are {x[2]}''')

name = input("Enter the name of the patient: \n").lower()
name = name.capitalize()
history = get_history(name)

if history != None:
    description(history)
else:
    print("Error: patient does not exist")