'''
Numpy --- Numpy is Memory Efficent and we can do fast computational operation.
Operation ---
1. Create Numpy Array ---  (Manual,buid in Function,Random Array)
2. DataType of numpy Array --- dtype
3. Access of Numpy Array
4. Slicing And fancy Index Concept  (Shared Memory or not)
'''


#1. Create Numpy Array


# Manual Process
import numpy as np

# 1- D Array (Vector)
a = np.array([1,2,3,4,5])
print("Number of Dimensions ",a.ndim)
print("Number of Length ",len(a))
print("Number of Shape ",a.shape)

# 2-D Array Matrix
b = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("Number of Dimensions ",b.ndim)
print("Number of Length ",len(b))
print("Number of Shape ",b.shape)

# Use Buildin arange Function

c = np.arange(10)  # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

one_Containg_numpy = np.ones([3,3])
'''
array([[1., 1., 1.],
       [1., 1., 1.],
       [1., 1., 1.]])
'''
zero_Containg_numpy = np.zeros([3,3])
'''
array([[0., 0., 0.],
       [0., 0., 0.],
       [0., 0., 0.]])
'''

# If random Array -- if you want to populate Random value in your numpy Array

#Uniform Distribution
d = np.random.rand(5)  #array([0.29392059, 0.94767182, 0.99932369, 0.13391767, 0.93395459])

# Normal Distribution
e = np.random.randn(3)  # array([ 0.95209573, -0.60127975,  2.182502  ])

# Interger in Specific Range
f = np.random.randint(1,20,5)  #  array([18, 11,  1,  5,  9])  1 to 20 5 Numbers i want


--------------------------------------------------------------------
# 2. DataType of numpy Array --- dtype
k = np.arange(10,dtype='float')   # array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.])



--------------------------------------------------------------------

# 3. Access of Numpy items
numpy_array = np.arange(1,20,2)
print(numpy_array[3])


--------------------------------------------------------------------
#4. play With index

# Shared Memory by two Array if we use concept Slicing

array1 =  np.arange(10)

array2 = array1[5:]

print(np.shares_memory(array1,array2))

# Problem is this Approch if i change in one Array then it will reflect in Another

array2[2] = 100
print(array1)  # [  0   1   2   3   4   5   6 100   8   9]


# So use Copy Function then your second array won't share memory let's try Again
array1 =  np.arange(10)
array2 = array1[5:].copy()
print(np.shares_memory(array1,array2))
array2[2] = 100
print(array1)  # [0 1 2 3 4 5 6 7 8 9]



# Concept of fancy indexing it won't share the memory

mask = (array1%2==0)
array3 = array1[mask]  # array([0, 2, 4, 6, 8])

print(np.shares_memory(array1,array3))









