'''
Hcf of two numbers
12 14 ---2


'''

def find_hcf_of(num1,num2):
    '''
    Calcute Lcf of two Number
    '''
    count = 0
    smallest = b if a>b else a 
    for i in range(1,smallest+1):
        if (a%i==0) and  (b%i==0):
            count = i
            print(count)
    return count


a = int(input(" Enter First Number ")) 
b = int(input(" Enter First Number "))   
x = find_hcf_of(a,b)
print("Hcf Of A Number is {}".format(x))

# How To Access Function Docs
print(find_hcf_of.__doc__)





