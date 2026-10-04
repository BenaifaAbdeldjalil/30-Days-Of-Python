# -*- coding: utf-8 -*-
""" 
## 💻 Exercises: Day 8

1. Create  an empty dictionary called dog
2. Add name, color, breed, legs, age to the dog dictionary
3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
4. Get the length of the student dictionary
5. Get the value of skills and check the data type, it should be a list
6. Modify the skills values by adding one or two skills
7. Get the dictionary keys as a list
8. Get the dictionary values as a list
9. Change the dictionary to a list of tuples using _items()_ method/pd.Series
10. Delete one of the items in the dictionary
11. Delete one of the dictionaries """



dog = {}
dog["name"] = "calvin"
dog["color"] = "black"
dog["breed"] = "berger"
dog["legs"] = "white"
dog["age"] = "5"
print(dog)

student = {
    'first_name':"djo",
    'last_name':"ben",
    'gender':"mal",
    'age':30,
    'marital status':"single",
    'skills':["ETL","FME", "PowerBI"],
    'country': "Algeria",
    'city': "Blida",
    'address' : { "number" : 16,
                 "type" : "av",
                 "name": "general de gaul",
                 'cp' : 69000,
                 'Town' : "Lyon"
    }
}
print(student)
print(len(student))
print(student.get('address','N/A'))
print(student.get('addr4ess','N/A')) #N/A

#student['skills'].append(["HTML","Python"])
student['skills'].append("HTML")
student['skills'].append("Python")
print(student.get('skills','N/A')) #N/A

print(student.items()) #N/A
print(student.values()) #N/A

import pandas as pd
print(pd.Series(student)) #N/A  

student.pop('marital status')
print(pd.Series(student)) #N/A  

dog.clear()

print(dog)