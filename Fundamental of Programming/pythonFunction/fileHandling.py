"""
File Handling Operation
    Our Python Code Always talk to operating System
    
Important Operation
1. Read File  (Copy)
2. Write File
3. Understanding of Direactory Managment
"""

file = open('my.txt','w')

file.write("My Name is Khan ")
file.write("I am not a telriost ")
file.write("Every Person is cool Here\n ")
file.write("I don't want to work here\n ")
file.write("Hey Sexy \n")

file.close()

#2. Reading is Something Important in NLP

file = open('my.txt','r')
print(file.read())

#Some Chuncks i want to read
file = open('my.txt','r')
print(file.read(5))
print(file.read(5))

# If you want to know Specific Location

print(file.tell())

# If You Want to Come on Specfic Location

file.seek(0)
print(file.read())


# Directory Managment of Understanding

import os
print(os.getcwd())

print(os.chdir("C:/Users/AITeam/Desktop"))

















