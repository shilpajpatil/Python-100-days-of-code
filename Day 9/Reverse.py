

def  rev():
    num = int(input("Enter a number:"))

    rev_num = 0

    while(num > 0):
        digit = num % 10;
        print("digit:",digit)
        rev_num = (rev_num *10) +digit
        print("rev_num",rev_num)
        num = num // 10
        print("num",num)
    print("The rev number is :", rev_num)