import pandas as pd

prefs = pd.read_csv("b1.csv")
prefs.to_dict()

print(prefs)

counts_pref = {1:[0,0,0],2:[0,0,0],3:[0,0,0],4:[0,0,0]}

for key,value in prefs.items():
    counts_pref[value[0]][0]+=1
    counts_pref[value[1]][1] += 1
    counts_pref[value[2]][2] += 1

course_to_discard = min([k[0] for k in counts_pref.items()])
li = [1,2,3,4]
li.remove(course_to_discard)
count_pref2 = {i:[0,0] for i in li}

for key,value in prefs.items():
    if value[0]==course_to_discard:
        count_pref2[value[1]][0]+=1
        count_pref2[value[2]][1]+=1

print(count_pref2)

