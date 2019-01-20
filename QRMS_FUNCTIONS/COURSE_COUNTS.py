def course_counts(pref_no,list_of_courses_to_cosider,student_preference_data):
    count_pref = {i:0 for i in list_of_courses_to_cosider["COURSE_ID"]}
    for student in student_preference_data.iterrows():
        count_pref[student[1]["PREF_"+str(pref_no)]]+=1
    return count_pref
