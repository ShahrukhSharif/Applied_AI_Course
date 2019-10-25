'''
Factorial of n --- 5 = 5*4*3*2*1
'''

def factoral(num):
    product = 1
    for i in range(1,num+1):
        product = product* i
    return product
        
print(factoral(5))


# Implement In Recursive Style
'''
fact(n) = n * fact(n-1)
fact(1) = 1
'''

def fact(num):
    return 1 if num==1 else (num*fact(num-1))

print(fact(5))


'''
Faboniici Series in python
0,1,1,2,3,5,8
fab(0) = 0
fab(1)=  1
fab(n) = fab(n-1)+ fab(n-2)
'''

def fab(num):
    a = 0
    b = 1
    c =0
    if(num==0) or (num==1):
        return num
    else:
        for i in range(2,num+1):
            c = a+b
            a = b
            b = c
        return c


for i in range(0,10):
    print(fab(i)," ")
    
    
# in the form of recursion
    

def fab(num):
    return num if num<=1 else (fab(num-1)+fab(num-2))

for i in range(10):
    print(fab(i))






    
    
