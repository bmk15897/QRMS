
from QRMS_FUNCTIONS import STUDENT_SORTING,COURSES_INITIAL_INFO
import pandas as pd

def allocate_courses_on_marks_over_preference(attribute_to_consider,student_data,student_prefs,courses):
    STUDENT_SORTING.sorting_on_an_attribute(attribute_to_consider,False,0,True,student_data)
    # print(student_data)
    courses1 = COURSES_INITIAL_INFO.courses_initial_info(courses)
    # print(courses)
    for i in student_data.iterrows():
        if student_prefs[i[1]["PRN"]].iloc[3]==i[1]["SEMESTER"]:
            for j in range(3):
                if courses1[student_prefs[i[1]["PRN"]].iloc[j]][2]>courses1[student_prefs[i[1]["PRN"]].iloc[j]][1]:
                    courses1[student_prefs[i[1]["PRN"]].iloc[j]][1]+=1
                    # student_data.loc[i[0]]["COURSE_ALLOTED"] = j
                    break
            # else:
            #     #assign the course with the maximum popularity
    df = pd.DataFrame([courses1[i][1] for i in range(len(courses1))])
    pd.concat(courses,df,ignore_index=True)
    print(courses1)


def allocation(attribute_to_sort,student_academic_data,student_preference_data,course_data):
    #sort students according to their marks
    STUDENT_SORTING.sorting_on_an_attribute(attribute_to_sort,False,0,True,student_academic_data)

    print(student_preference_data)

    course_data = COURSES_INITIAL_INFO.courses_initial_info(course_data)
    print(course_data)

    alloted_courses = {}

    #traversing through all the students
    for student in student_academic_data.iterrows():
        #check if the student has entry in student preference data by matching SEMESTER

        print(student)
        print(type(student))

        student1 = student_preference_data.loc[student[0],:].copy()
        print(student1)
        print(type(student1))

        #check if the student is from that branch and from that semester and from that year

        # break
        if  student[1]["SEMESTER"]==student1["SEMESTER"]:
            print("yes")
            student1.drop("SEMESTER",inplace=True)
            for pref in student1:
                print(pref)
                if course_data[pref][1]<course_data[pref][2]:
                    course_data[pref][1]+=1
                    student[1]["COURSE_ALLOTED"] = pref
                    alloted_courses[student[0]] = pref
                    print(student)
                    break
                else:
                    print("Cannot allocate!")   #need to find an alternative to this
    return alloted_courses