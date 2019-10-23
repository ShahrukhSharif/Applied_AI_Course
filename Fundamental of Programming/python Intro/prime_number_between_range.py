# Wap to  Prime Number between Range

'''
num = 10
10/2,3,4,5 ---> Number is not pN OW PN
'''


num1 = int(input("Input the Number1 "))
num2 = int(input("Input the Number2"))

for i in range(num1,num2+1):
    is_divisible = False
    for k in range(2,i):
        if(i%k==0):
            is_divisible = True
            break
    if is_divisible is False:
        print("Number is PN {}".format(i))
