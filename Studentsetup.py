import sqlite3
conn = sqlite3.connect("company.db")
from random import randint,randrange
from datetime import date

store = conn.cursor()

# Build all lists for lastNames, maleNames, femaleNames, departments, genders
lastNames = ["Han","Peter","Ho","Thomsas","Schmidt","Christian","Smith","Johnny","Williams","Brown","Jones","Miller","Erza","James","Peterota","Rich","Valentina","Boyd","Ester","Morris","Bryan","Marquez","Simon","Klaus","Lindsey","Shaw","Cisnero","Haydon","Pope","Sam","Stewart","Perry"]
maleNames = ["James","Jacob","Robert","Mike","William","Derek","Richard","Derrick","Walter","Patty","Peter","Darnell","Jack","Terrance","Daniel","Jacob","Smith","Ryan","Gary","Jacobson","Nicholas","Ericson","Stephen","Jonathanson","Larry","Justin","Scotty","Frank","Brandon","Raymonda","Gregory","Benjamina","Samuel","Patricky","Alexander"]
femaleNames = ["Maryah","Patricia","Lindah","Barbara","Elizabetha","Jenniferah","Kareny","Judy","Ireney","Janey","Lori","Judy","Rubyah","Lois","Tina","Emmah","Olivia","Ava","Isabella","Sophiah","Mia","Amelia","Charlotte","Abigail","Emilyah","Arlene","Maureen","Collen","Allison","Tamara","Joy","Georgia","Constance","Lillie","Claudia"]
names = [maleNames,femaleNames]
departments = ["IT","Sales","HR","Marketing","Research"]
genders = ["M","W"]
students = []

# Genereate 30 Employees with random attributes
for index in range(30):
    lastName = lastNames[randint(0,31)]
    gender = randint(0,1)
    firstName = names[gender][randint(0,34)]
    sex = genders[gender]
    age = randint(18,62)
    birthdate = date((2018 - age), randint(1,12), randint(1,28)).isoformat()
    work_load = randrange(15,40,5)
    work_group = departments[randint(0,4)]
    student = (index,firstName,lastName,birthdate,age,sex,work_load,work_group)
    print(student)
    students.append(student)

# Drop previous Table
store.execute('''DROP TABLE employees''')

# Create new Table
store.execute('''CREATE TABLE employees
             (id integer primary key autoincrement, firstname text, lastname text, birthdate text, age integer, sex text, workload_per_week real, work_group text)''')

# Insert a all 30 rows of data
store.executemany('INSERT INTO employees VALUES (?,?,?,?,?,?,?,?)', students)

# Save (commit) the changes
conn.commit()

conn.close()