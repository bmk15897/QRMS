import sqlite3 as sql

db = "test.db"

con = sql.connect(db)
c = con.cursor()

# c.execute("CREATE TABLE STUD_DETS(PRN INT,NAME VARCHAR,SEM INT,MARKS INT,ALLOTED_COURSE INT);")
# c.execute("CREATE TABLE STUD_PREFS(PRN INT,SEM INT,PREF1 INT,PREF2 INT,PREF3 INT);")

import pandas as pd

data = pd.read_excel("/home/bharati/Desktop/data.xlsx")

data1 = data.iloc[:216,0:2]
data2 = data.iloc[:216,35]
data = pd.concat([data1,data2],axis=1,join='inner')
data["PRN"].apply(lambda x:int(x))
data["MARKS"].apply(lambda x:float(x))


# import numpy as np
#
# data = data[data.MARKS!=np.nan]
# print(data.shape)
#


'''

# print(data)

# for i in data:
#     print(i)
    # PRN =
    # c.execute("INSERT INTO STUD_DETS(PRN,NAME,SEM,MARKS) VALUES({0},{1},{2},{3});".format(PRN,NAME,7,MARKS))

query = "INSERT OR REPLACE INTO STUD_DETS(PRN,NAME,SEM,MARKS) VALUES(?,?,7,?);"
con.executemany(query,data.to_records(index=False))
con.commit()

d = con.execute("SELECT * FROM STUD_DETS;").fetchall()
print(d)
'''


# print(data)


import secrets

data.sort_values(by=["MARKS"],ascending=False,axis=0,inplace=True)
data.drop(index=[0,148,149],axis=1,inplace=True)
print(data)

print(data)
prefs = {}
choices = [1,2,3,4]

for i,student in data.iterrows():
    list = [1,2,3,4]
    pref1 = secrets.choice(list)
    prefs[student["PRN"]] = [pref1]
    list.remove(pref1)
    pref2 = secrets.choice(list)
    prefs[student["PRN"]].append(pref2)
    list.remove(pref2)
    pref3 = secrets.choice(list)
    prefs[student["PRN"]].append(pref3)
    list.remove(pref3)


print(prefs)


counts_pref = {1:[0,0,0],2:[0,0,0],3:[0,0,0],4:[0,0,0]}

for key,value in prefs.items():
    counts_pref[value[0]][0]+=1
    counts_pref[value[1]][1] += 1
    counts_pref[value[2]][2] += 1

print(counts_pref)

course_to_discard = min([k[0] for k in counts_pref.items()])

print(course_to_discard)

try1 = pd.DataFrame(prefs)

try1.to_csv("b1.csv",sep=",",encoding="utf-8")