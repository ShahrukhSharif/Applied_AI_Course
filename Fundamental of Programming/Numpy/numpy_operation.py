# numpy Operation

# 1. Brodcasting Operation
'''
If Array Size is not same,numpy Array try to Adjust size and Perform numpy
Operation Column Wise
'''

import numpy as np

z1 = np.arange(0,40,10)  # array([ 0, 10, 20, 30])

print('Size of Numpy Array ',np.shape(z1))
print('Dimensions of Numpy Array',z1.ndim)

z1 = z1[:,np.newaxis]

print('Size of Numpy Array ',np.shape(z1))
print('Dimensions of Numpy Array',z1.ndim)

'''
array([[ 0],
       [10],
       [20],
       [30]])
'''


z2 = np.arange(0,40,10)

print(z1+z2)

'''
[[ 0 10 20 30]
 [10 20 30 40]
 [20 30 40 50]
 [30 40 50 60]]
'''


# 2. ravel,reshape,resize   (Flat Array,Change in Dimensions,Change the size)

r1 =  np.arange(0,100,10)

r2 = np.reshape(r1,(2,5))

r3 = np.ravel(r2)

r4 = np.resize(r3,(16,))  # [ 0 10 20 30 40 50 60 70 80 90  0 10 20 30 40 50]

'''
reshape function is sometimes give copy and sometimes it's not
resize function Sometimes create some refrence Problem So be Craefull
'''

# 3. Comparision And Sorting

n1 = np.array([4,3,2,1])
n2 = np.array([5,6,7,8])

print(np.array_equal(n1,n2))

# Sorting of an Numpy Array

z1 = np.sort(n1,axis=-1)
print(z1)


# Another Way of sorting

c = np.argsort(z1,axis=-1)
print(z1[c])














