# -*- coding: utf-8 -*-
#Exercises: Level 1
from pathlib import Path

base = "/data/"
file_obama = ["obama_speech.txt",
              "michelle_obama_speech.txt",
              "melina_trump_speech.txt",
              "donald_speech.txt"]

"""
for i in file_obama:
    file = Path("."+base+i)
    with  file.open('r' , encoding="utf-8") as f :
        lines = f.readlines()
        content = f.read()# mode(r, a, w, x, t,b)
        words=content.split(" ")
        #print(f'extrait : {words}')
        #lines = f.readlines()
    with  file.open('r' , encoding="utf-8") as f :
        content = f.read()# mode(r, a, w, x, t,b)
        words=content.split()

    #print(len(content),f) #caractere
    #print(f'nombre de mots  : {len(words),f}') #words
    #print(len(lines),f) #lignes

"""
#Read obama_speech.txt file and count number of lines and words
#Read michelle_obama_speech.txt file and count number of lines and words
#Read donald_speech.txt file and count number of lines and words
#Read melina_trump_speech.txt file and count number of lines and w

"""
#Exercises: Level 2 : 
#email
import re
from collections import Counter

file_mail = ["email_exchanges_big.txt"]
file_m= Path("."+base+file_mail[0])
# pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'


with  file_m.open('r' , encoding="utf-8") as f :
    content = f.read()# mode(r, a, w, x, t,b)
    emails = re.findall(pattern, content)
    print(emails)

def find_most_common_words(file,i):
    tp=()
    with  file_m.open('r' , encoding="utf-8") as f :
        content = f.read()# mode(r, a, w, x, t,b)
        # words = re.findall(r"\b\w+\b", content.lower())
        counts = Counter(words)
        result = list(counts.items())
        sorted_result = sorted(result, key=lambda x: x[1], reverse=True)
        
    # print(sorted_result[:i])


find_most_common_words(file_m,10) """


import re
from collections import Counter

file_h = "hacker_news.csv"
file_hacker = Path("."+base+file_h)
pattern = ['python','Python']

"""
with  file_m.open('r' , encoding="utf-8") as f :
    content = f.read()# mode(r, a, w, x, t,b)
    emails = re.findall(pattern, content)
    print(emails)"""


def hacker(file):
    python_count = 0
    javascript_count = 0
    java_count = 0
    tp=()
    with  file.open('r' , encoding="utf-8") as f :
        for line in f:
            # Python or python
            if "python" or 'Python' in line.lower():
                python_count += 1

            # JavaScript, javascript, Javascript
            if "javascript" in line.lower():
                javascript_count += 1

            # Java, excluding JavaScript
            if "java" in line.lower() and "javascript" not in line.lower():
                java_count += 1
    return python_count, javascript_count, java_count
    print("###############")
python_lines, javascript_lines, java_lines = hacker(file_hacker)

print(f"Lines containing Python or python: {python_lines}")
print(f"Lines containing JavaScript/javascript/Javascript: {javascript_lines}")
print(f"Lines containing Java but not JavaScript: {java_lines}")