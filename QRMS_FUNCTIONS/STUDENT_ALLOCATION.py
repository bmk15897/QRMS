
from QRMS_FUNCTIONS import STUDENT_SORTING,COURSES_INITIAL_INFO,COURSE_COUNTS
from operator import itemgetter

def allocation(attribute_to_sort,student_academic_data,student_preference_data,course_data):
    #sort students according to their marks
    STUDENT_SORTING.sorting_on_an_attribute(attribute_to_sort,False,0,True,student_academic_data)

    # print(student_preference_data)

    course_data = COURSES_INITIAL_INFO.courses_initial_info(course_data)
    # print(course_data)

    alloted_courses = {}

    list_of_courses = course_data.keys()
    # count the course preferences, calculate the popularity of each in descending order
    course_popularity = COURSE_COUNTS.course_preference_counts_dict(1,list_of_courses, student_preference_data)
    # print(course_popularity)

    course_popularity = [(k, v) for k, v in sorted(course_popularity.items(), key=itemgetter(1), reverse=True)]

    print(course_popularity)

    #traversing through all the students
    for student in student_academic_data.iterrows():
        #check if the student has entry in student preference data by matching SEMESTER

        # print(student)
        # print(type(student))

        student1 = student_preference_data.loc[student[0],:].copy()
        # print(student1)
        # print(type(student1))

        #check if the student is from that branch and from that semester and from that year

        if  student[1]["SEMESTER"]==student1["SEMESTER"]:
            # print("yes")
            student1.drop("SEMESTER",inplace=True)
            for pref in student1:
                # print(pref)
                if course_data[pref][1]<course_data[pref][2]:
                    course_data[pref][1]+=1
                    student[1]["COURSE_ALLOTED"] = pref
                    alloted_courses[student[0]] = pref
                    # print(student)
                    break
            else:
                # print("Cannot allocate!")   #need to find an alternative to this
                for remaining_course in course_popularity:
                    if course_data[remaining_course[0]][1]<course_data[remaining_course[0]][2]:
                        course_data[remaining_course[0]][1] += 1
                        student[1]["COURSE_ALLOTED"] = remaining_course[0]
                        alloted_courses[student[0]] = remaining_course[0]
                        break
    return alloted_courses