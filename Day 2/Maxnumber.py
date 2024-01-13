

def maxnumber():
    num1= int(input("Enter a numebr"));
    num2=int(input("Enter a second number"))
    num3 = int(input("Enter a third number:"))

    if(num1 < num2):
        print(num2 ,"is greater")
    elif(num2 < num3):
        print(num3, "is greater")
    else:
        print(num1,"is greater")
