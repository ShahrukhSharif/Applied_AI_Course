'''
Exception Handling ---
Python Interpretor raise Error we want to handle Grasefully.
'''

import sys

list = ['a',0,3]

for i in list:
    try:
        x = 3/i
        print("Division is ",x)
    except:
        print("Error Name is ",sys.exc_info()[0])
        
        
        
# We can Also Handle the Errors
        
for i in list:
    try:
        x= 3/i
        print("Division is ",x)
    except(TypeError):
        print("Don't devide by laters")
    except(ZeroDivisionError):
        print("Don't devide by zero")
    except:
        print("No Error")
        
        

# We can Also Raise the Exception
a = int(input("Enter The Number"))
try:
    if a<=0:
        raise ValueError("Don't enter Negetive Numbers")
except ValueError as m:
    print(m)
    

# finally Block
    
try:
    file = open('my.txt','r')
finally:
        file.close()
        print("This is always run")
        
    
        
    
