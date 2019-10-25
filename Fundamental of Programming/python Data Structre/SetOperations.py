'''
Sets Are Unordered Collection of items. Menas we can't index
Set Doesn't allow repeated Value
'''

# Set Operations 

# 1. Union |

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

set3 = set1 | set2
print(set3)   #{1, 2, 3, 4, 5, 6, 7, 8}

# 2 . Intersaction &
set3 = set1 & set2
print(set3)   #{4, 5}

# 3.  Set Diffrence - 
set3 = set1 - set2
print(set3)  # {1, 2, 3}

# 4. Symettric Diffrence ^
set3 = set1 ^ set2
print(set3)  # {{1, 2, 3, 6, 7, 8}}
