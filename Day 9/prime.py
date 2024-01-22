

# Append new string middle of two strings:

def primenum():
    flag = 0
    m=0
    num = int(input("Enter a number:"))
    if(num==1):
        flag=1
        print("Not a prime")
    for i in range(2,num **(1//2)+1):
        if (num%i==0):
            print("Not Prime")
            flag=1
            break;


    if (flag == 0):
        print("prime")
