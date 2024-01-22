

#Accept a number from user and print the number is armstrong or not

def username():

    num = int(input("enter a number:"))
    print(num)


    arm = armstrong(num)
    if arm == 1:
        print(num,"is not armstrong")
    else:
        print(num,"is a armstrong")

def armstrong(num):
    total = 0
    while(num !=0):
        digit = num %10
        print(digit ,"\n")

        total = total + (digit*digit*digit)
        num = num//10;

    print("Total is:",total)
    if num == total:
        return 1;
    else:
        return 0;