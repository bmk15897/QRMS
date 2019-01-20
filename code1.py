import pandas as pd
import sys

from QRMS_FUNCTIONS import COURSE_COUNTS,STUDENT_ALLOCATION

data = pd.read_excel("/home/bharati/Desktop/data.xlsx")

data["PRN"].apply(lambda x:int(x))
data["MARKS"].apply(lambda x:float(x))


# print(data)
data.set_index("PRN",inplace=True)
# print(data)

# print(data.loc[2,:])

prefs = pd.read_csv("b1.csv",header=None)
prefs.columns = ["PRN","PREF_1","PREF_2","PREF_3","SEMESTER"]

prefs.set_index("PRN",inplace=True)


courses = pd.read_excel("/home/bharati/Desktop/course_data.xlsx")


#   You can use the below way to find the counts for preferences for each course
# pref_no_to_count = 1
# course_counts = COURSE_COUNTS.course_preference_counts_dataframe(pref_no_to_count,courses,prefs.copy())
# print(course_counts)

alloted_courses = STUDENT_ALLOCATION.allocation("MARKS",data,prefs,courses)

# print(alloted_courses)

allocated_counts = COURSE_COUNTS.course_allocation_counts_dict(alloted_courses)
print(allocated_counts)

for key,value in alloted_courses.items():
    data.loc[key,"COURSE_ALLOTED"]=value

# print(data)

