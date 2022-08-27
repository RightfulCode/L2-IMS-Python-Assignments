#Task 8
'''Here our client has sent out 5 teams each to a specific region. In each region, they visted 9 schools
and held a survey to see how much of the youth agreed with the current political situation. They then
returned the percentage of students in agreement from each school. We are tasked with finding out the
average of each region and then of all the regions combined'''
info_first = {10,20,22,13,14,78,64,55,100}
info_second = {30,20,33,41,2,83,99,21,17}
info_third = {49,56,72,14,25,26,91,0,10}
info_fourth = {80,98,100,57,66,89,60,100,92}
info_fifth = {0,2,1,5,10,40,32,89,24}

list_first = list(info_first)
n = 0
for i in list_first:
    n += i
first_region_percentage = round(n/len(info_first),1)

list_second = list(info_second)
n = 0
for i in list_second:
    n += i
second_region_percentage = round(n/len(info_second),1)

list_third = list(info_third)
n = 0
for i in list_third:
    n += i
third_region_percentage = round(n/len(info_third),1)

list_fourth = list(info_fourth)
n = 0
for i in list_fourth:
    n += i
fourth_region_percentage = round(n/len(info_fourth),1)

list_fifth = list(info_fifth)
n = 0
for i in list_fifth:
    n += i
fifth_region_percentage = round(n/len(info_fifth),1)

all_info = info_first.union(info_second,info_third,info_fourth,info_fifth)
all_list = list(all_info)
n = 0
for i in all_list:
    n += i
all_percentage = round(n/len(all_info),1)

print(f'''{first_region_percentage}% of youngsters agree in the first region.
{second_region_percentage}% of youngsters agree in the second region.
{third_region_percentage}% of youngsters agree in the third region.
{fourth_region_percentage}% of youngsters agree in the fourth region.
{fifth_region_percentage}% of youngsters agree in the fifth region.
Overall, {all_percentage}% of the youth agree with the current politics''')