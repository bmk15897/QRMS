import pandas as pd
import sys

from QRMS_FUNCTIONS import COURSE_COUNTS,STUDENT_ALLOCATION,COURSES_INITIAL_INFO

#take all the inputs

#take student academic data

data = pd.read_excel("/home/bharati/Desktop/data.xlsx")

data["PRN"].apply(lambda x:int(x))
data["MARKS"].apply(lambda x:float(x))

data.set_index("PRN",inplace=True)


print("***********************STUDENT ACADEMIC DETAILS**********************************")
print()
print()

print(data)
print()
print()

#take student preferences data

prefs = pd.read_csv("b1.csv",header=None)
prefs.columns = ["PRN","PREF_1","PREF_2","PREF_3","SEMESTER"]

prefs.set_index("PRN",inplace=True)

print("***********************STUDENT PREFERENCE DETAILS**********************************")
print()
print()

print(prefs)
print()
print()

#take courses data

courses = pd.read_excel("/home/bharati/Desktop/course_data.xlsx")

print("***********************COURSE DETAILS**********************************")
print()
print()

print(courses)
print()
print()

pref_no_to_count = 1
course_counts = COURSE_COUNTS.course_preference_counts_dataframe(pref_no_to_count,courses,prefs.copy())

print("***********************STUDENT FIRST PREFERENCE COUNT DETAILS**********************************")
print()
print()

print(course_counts)
print()
print()

pref_no_to_count = 2
course_counts = COURSE_COUNTS.course_preference_counts_dataframe(pref_no_to_count,courses,prefs.copy())

print("***********************STUDENT SECOND PREFERENCE COUNT DETAILS**********************************")
print()
print()

print(course_counts)
print()
print()

pref_no_to_count = 3
course_counts = COURSE_COUNTS.course_preference_counts_dataframe(pref_no_to_count,courses,prefs.copy())

print("***********************STUDENT THIRD PREFERENCE COUNT DETAILS**********************************")
print()
print()

print(course_counts)
print()
print()

unallocated_counts = COURSES_INITIAL_INFO.courses_initial_info(courses)

print("***********************INITIAL COURSE COUNT DETAILS**********************************")
print()
print()

print(unallocated_counts)
print()
print()


alloted_courses = STUDENT_ALLOCATION.allocation("MARKS",data,prefs,courses)

for key,value in alloted_courses.items():
    data.loc[key,"COURSE_ALLOTED"]=value

print("***********************STUDENT ALLOCATION DETAILS**********************************")
print()
print()

print(data)
print()
print()

allocated_counts = COURSE_COUNTS.course_allocation_counts_dict(alloted_courses)

print("***********************FINAL COURSE COUNT DETAILS**********************************")
print()
print()

print(allocated_counts)
print()
print()


print("END")