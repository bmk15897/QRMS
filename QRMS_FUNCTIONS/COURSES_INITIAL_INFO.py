def courses_initial_info(courses):
    courses_seats_alloted = {}
    for i in courses.iterrows():
        courses_seats_alloted[i[1]["COURSE_ID"]] = [i[1]["SEMESTER"],i[1]["ALLOTED_SEATS"],i[1]["COURSE_SEATS"]]
    return courses_seats_alloted