'''
String ---   
1. Sequence Of Character
2. Immutable
'''

mystr = "My Gf Name is Namrata"

# 1. How many time later a is repeted
count = 0
for i in mystr:
    if i=='a':
        count+=1

print("Number of later a is {}".format(count))


# 2. String Function Split and join

love = "my love is namrata only"
love.split()   # ['my', 'love', 'is', 'namrata', 'only']


c1 = ['my', 'love', 'is', 'sahina', 'only']
c2 = ' '.join(c1)
print(c2)


# 3. Palindrome or not

plnd = 'Madamjk'
plnd = plnd.lower()
plnd1 = list(plnd)
plnd1.reverse()
         
if plnd1==list(plnd):
    print("String is Palindrome")
else:
    print("String is not palindrome")



# 4. sort a string
    
string_ab = "my love is namrata only"

a = string_ab.split()

a.sort()

b = ' '.join(a)   # 'is love my namrata only'















