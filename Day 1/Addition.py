
# This program contains logic of calculator

def addition():
    num1 = int(input("Enter a number:"))
    num2 = int(input("Enter a second number:"))
    add = num1+num2
    print ("Addition of ", num1 ,"and", num2 ,"=:",add)
    sub = subtraction(num1,num2)
    print("Subtraction of ", num1, "and", num2, "=:", sub)
    mul =Multiplication(num1,num2)
    print("Multiplication of ", num1, "and", num2, "=:", mul)
    div = Division(num1,num2)
    print("Division of ", num1, "and", num2, "=:", div)


def subtraction(num1,num2):

    sub = num1-num2
    return sub

def Multiplication(num1,num2):

        mul = num1 * num2
        return mul

def Division(num1,num2):

    div = num1 % num2
    return div
