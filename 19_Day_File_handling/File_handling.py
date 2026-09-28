# -*- coding: utf-8 -*-
from pathlib import Path


file = "19_Day_File_handling/file.txt"

f = open(file, "r", encoding="utf-8")
print(f.read())

print("############################################")
#OR
file = Path("19_Day_File_handling/file.txt")

with  file.open('r' , encoding="utf-8") as f :
    content = f.read()# mode(r, a, w, x, t,b)
    f.close()
print(content) 
print("############################################")

# output
print(type(content) )
"""
<class 'str'>
This is an example to show how to open a file and read.
This is the second line of the text.
"""


#readline(): read only the first line
f = open(file, "r", encoding="utf-8")
content =f.readline()
f.close()
print(content)

#readline(): read all the text line by line and returns a list of lines
f = open(file, "r", encoding="utf-8")
content =f.readlines()
f.close()
print(content)
print(type(content))
# output
"""<class 'list'>
['This is an example to show how to open a file and read.\n', 'This is the second line of the text.']"""


#Opening Files for Writing and Updating
#append  
with open(file,'a') as f:
    f.write('This text has to be appended at the end')

with  file.open('r' , encoding="utf-8") as f :
    content = f.read()# mode(r, a, w, x, t,b)
    f.close()
print(content)

#creating file
#The method below creates a new file, if the file does not exist:
new_file="19_Day_File_handling/new_file.txt"
with open(new_file,'w') as f:
    f.write('This text will be written in a newly created file')
#creatin if not existe else update
import os
new_f="19_Day_File_handling/if_exist_new_file.txt"
if not os.path.exists(new_f):
    with open(new_f,'w') as f:
        f.write('This text will be written in a newly created file')
        print(f" {new_f}  creé !")
else:
    with open(new_f,'a') as f:
        f.write('This text has to be appended at the end \n' ) 
        print(f" {new_f} existe deja !") 
#Deleting Files
import os
os.remove('./19_Day_File_handling/new_file.txt')

#remouve if existe
import os
if os.path.exists('./19_Day_File_handling/new_file.txt'):
    os.remove('./19_Day_File_handling/new_file.txt')
else:
    print('The file does not exist')


# dictionary
person_dct= {
    "name":"benaifa",
    "country":"Algeria",
    "city":"blida",
    "skills":["JavaScrip", "React","Python"]
}


new_dic="19_Day_File_handling/person_dct.json"
if not os.path.exists(new_dic):
    with open(new_dic,'w') as f:
        f.write(f''''{person_dct}''''')
        print(f" {new_dic}  creé !")
else:
    with open(new_dic,'a') as f:
        f.write("''' \n" ) 
        f.write(f'{person_dct}')
        f.write("''' \n" ) 


### Changing JSON to Dictionary

import json
# JSON
person_json = '''{
    "name": "benaifa",
    "country": "Algeria",
    "city": "blida ",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])


### Changing Dictionary to JSON

#To change a dictionary to a JSON we use _dumps_ method from the json module.

import json
# python dictionary
person = {
    "name": "benaifa",
    "country": "Algeria",
    "city": "blida",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
print(person_json)


### Saving as JSON File

#We can also save our data as a json file. Let us save it as a json file using the following steps. For writing a json file, we use the json.dump() method, it can take dictionary, output file, ensure_ascii and indent.

import json
# python dictionary
person = {
    "name": "benaifa",
    "country": "Algeria",
    "city": "blida",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./19_Day_File_handling/json_text.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)




### File with csv Extension

#CSV stands for comma separated values. CSV is a simple file format used to store tabular data, such as a spreadsheet or database. CSV is a very common data format in data science.



""" 
"name","country","city","skills"
"benaifa","Algeria","blida","JavaScript"

"""

import csv
with open('./19_Day_File_handling/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # we use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')

""""
Column names are :name, country, city, skills
        benaifa is a teachers. He lives in Algeria, blida.
Number of lines:  2
"""

### File with xml Extension

#XML is another structured data format which looks like HTML. In XML the tags are not predefined. The first line is an XML declaration. The person tag is the root of the XML. The person has a gender attribute.


"""

xml
<?xml version="1.0"?>
<person gender="female">
  <name>Asabeneh</name>
  <country>Finland</country>
  <city>Helsinki</city>
  <skills>
    <skill>JavaScrip</skill>
    <skill>React</skill>
    <skill>Python</skill>
  </skills>
</person>

 """


import xml.etree.ElementTree as ET
tree = ET.parse('./19_Day_File_handling/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)
