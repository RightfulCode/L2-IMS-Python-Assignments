#Task 9
'''The client has provided us with a set of jumbled up data of different types. Our task is to organize
the data by their types and store them into different sets.'''
thisset = {"ali",12,3,4,5,"ammar","araiz",2,"adil",8,7,100,True,False,3.0,5.55,60.8}

thislist = list(thisset)
int_list = [x for x in thislist if type(x) == int]
str_list = [x for x in thislist if type(x) == str]
float_list = [x for x in thislist if type(x) == float]
bool_list = [x for x in thislist if type(x) == bool]

int_set = set(int_list)
str_set = set(str_list)
float_set = set(float_list)
bool_set = set(bool_list)

print(int_set)
print(str_set)
print(float_set)
print(bool_set)