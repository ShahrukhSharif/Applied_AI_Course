'''
Space And Time Complexity
'''

# 1. If List is not Sorted The Use Naive Approch For Search

list1 = list(range(50))
import random
random.shuffle(list1)

for i in list1:
    flags = False
    if i == 31:
        flags = True
        break
    
if flags == True:
    print("list element Found")
else:
    print("List Element Not Found")
    
    
# 2 . If List is Sorted then use This Approch or if you are again and again
# Searching Something then this one is also Good
    
    
list1 = list(range(1000))
def binary_search(arr1,l,r,value):
    print("Value of l",l)
    print("Value of r",r)
    if r>=1:
        import math
        m = l + math.floor((r-1)/2)
        if arr1[m]>value:
            r = m-1
            binary_search(arr1,l,r,value)
        elif arr1[m]<value:
            l = m+1
            binary_search(arr1,l,r,value)
        else:
            return m
    else:
        return 0

print(binary_search(list1,0,len(list1)-1,29))


# if you have two list find common items
list1 = list(range(0,100))
import random
random.shuffle(list1)


list2 = list(range(80,140))
import random
random.shuffle(list2)

count =0
for i in list1:
    for j in list2:
        if i == j:
            print("Comman Value is",i)
            count+=1
            
print("Total Comman Values ",count)


# Using Dectionary Search A element




dicts ={}

for i in list2:
    dicts[i] = 1
            
for i in list1:
    if dicts.get(i)!=None:
        print("Coumn Value is ",i)


    
