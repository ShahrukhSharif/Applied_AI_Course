# List
'''
Collection of items,
Each item in list has index value
List are Mutable
'''


# Some Operation in list

# 1. Diffrence between Append And Extend And +


list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

list1.append(list2)
print(list1)   # [1, 2, 3, 4, 5, [6, 7, 8, 9, 10]]


list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
list1.extend(list2)
print(list1)   #[1,2,3,4,5,6,7,8,9,10]

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
z = list1+list2
print(z)      # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 6, 7, 8, 9, 10]


# 2. Freqency of a element inside a column

list1 =[1,2,3,4,5,1,2,3,1,2,1,1]
print(list1.count(1))    #5


# 3. comprehension in python

square = []
for i in range(10):
    square.append(i**2)
print(square)    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


square1 = [i**2 for i in range(10)]
print(square)    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# More Complex Example Of Matrix Comprehension

matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]

transpose = []
for i in range(4):
    x = []
    for y in matrix:
        x.append(y[i])
    transpose.append(x)
    
    
print(transpose)

transpose1 = [[i[m] for i in matrix] for m in range(4) ]
print(transpose1)



        
    
