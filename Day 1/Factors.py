

def factors():
    num = int(input("Enter a number:"))

    list1=[]
    for i in range(1,num+1):
        if(num%i == 0):
            list1.append(i)
           # print("number ", num , "divisible by", i)

    print("Factors of", num, "is:",list1)