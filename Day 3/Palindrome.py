
# Using For loop

def palindrome():
    num = int(input("enter a number:"))

    revnum = 0
    temp = num;
    while(num>0):

        digit=num % 10;
        print("digit:",digit)

        revnum = revnum * 10 + digit
        print("revnum:",revnum)
        num = num // 10
        print("num:",num)
    if(temp == revnum):
        print(temp,"is  a palindrome")
    else:
        print(temp ,"is not a  palindrome")





