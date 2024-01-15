
def revlist():

    mylist = []
    size = int(input("Enter a size of a list:"))
    for i in range(size):
        num = input("enter items to add in a list")
        mylist.append(num)

    print("User created list:",mylist)
    print("reverse list is: ",mylist[::-1])