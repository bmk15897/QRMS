def course_preference_counts_dataframe(pref_no,list_of_courses_to_cosider,student_preference_data):
    count_pref = {i:0 for i in list_of_courses_to_cosider["COURSE_ID"]}
    for student in student_preference_data.iterrows():
        count_pref[student[1]["PREF_"+str(pref_no)]]+=1
    return count_pref

def course_preference_counts_dict(pref_no,list_of_courses_to_cosider,student_preference_data):
    count_pref = {i:0 for i in list_of_courses_to_cosider}
    for student in student_preference_data.iterrows():
        count_pref[student[1]["PREF_"+str(pref_no)]]+=1
    return count_pref

def course_allocation_counts_dict(student_allocation_data):
    count_allocated = {i:0 for i in set(student_allocation_data.values())}
    for value in student_allocation_data.values():
        count_allocated[value]+=1
    return count_allocated
