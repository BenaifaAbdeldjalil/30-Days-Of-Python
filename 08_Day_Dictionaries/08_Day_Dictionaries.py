# -*- coding: utf-8 -*-
person = {
    'first_name':'Djalil',
    'last_name':'Benaifa',
    'age':250,
    'country':'Algeria',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

print(person)



person = {
    'first_name':'Djalil',
    'last_name':'Benaifa',
    'age':250,
    'country':'Algeria',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(len(person)) # 7

person = {
    'first_name':'Djalil',
    'last_name':'Benaifa',
    'age':250,
    'country':'Algeria',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person['first_name']) # Djalil
print(person['country'])    # Algeria
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
#print(person['city'])       # Error KeyError: 'city'


person = {
    'first_name':'Djalil',
    'last_name':'Benaifa',
    'age':250,
    'country':'Algeria',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person.get('first_name')) # Djalil
print(person.get('country'))    # Algeria
print(person.get('skills')) #['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None



person = {
    'first_name':'Djalil',
    'last_name':'Benaifa',
    'age':250,
    'country':'Algeria',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
        }
}
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)


person = {
    'first_name':'Djalil',
    'last_name':'Benaifa',
    'age':250,
    'country':'Algeria',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
person['first_name'] = 'Eyob'
person['age'] = 252

person = {
    'first_name':'Djalil',
    'last_name':'Benaifa',
    'age':250,
    'country':'Algeria',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
person.pop('first_name')        # Removes the firstname item
person.popitem()                # Removes the address item
del person['is_married']        # Removes the is_married item 