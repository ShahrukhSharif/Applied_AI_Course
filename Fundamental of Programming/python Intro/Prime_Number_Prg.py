# Wap to find Prime Number

'''
num = 10
10/2,3,4,5 ---> Number is not pN OW PN
'''



num = int(input("Input the Number"))
is_devisible = False

for i in range(2,num):
    if(num%i==0):
        is_devisible = True
        break
    
if is_devisible is True:
    print("Number is Not Prime {}".format(num))
else:
    print("Number is Prime Number {}".format(num))
