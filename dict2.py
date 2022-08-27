#Task 8
'''Here our client has asked us to create a program which lets us enter, and store the data of the patient
in a dictionary to be accessed later.'''
patients = {}
name = input("Enter the name: \n").lower()
name = name.capitalize()

day_of_admit = input("Enter the day when the patient was admitted: \n")
month_of_admit = input("Enter the month of admit: \n").capitalize()
year_of_admit = input("Enter the year of admit: \n")
date_of_admit = f"{day_of_admit} {month_of_admit},{year_of_admit}"

day_of_exit = input("Enter the day when the patient left: (leave empty if still admitted)\n")
month_of_exit = input("Enter the month of exit: (leave empty if still admitted)\n").capitalize()
year_of_exit = input("Enter the year of exit: (leave empty if still admitted)\n")
if len(day_of_exit) == 0 and len(month_of_exit) == 0 and len(year_of_exit) == 0:
    date_of_exit = "Still admit"
else:
    date_of_exit = f"{day_of_exit} {month_of_exit},{year_of_exit}"
medicine = input("Please enter medicine: \n").lower()
medicine = medicine.capitalize()

patient_list = [date_of_admit,date_of_exit,medicine]
patients[name] = patient_list
print(patients)