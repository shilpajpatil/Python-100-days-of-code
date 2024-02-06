

# copying one file data into another

def fileread3():

    firstfile = input("Enter the name of first file:")
    secondfile = input("Enter the name of second file:")

    # opening both files  in read only
    f1 =open(firstfile,'r')
    f2 = open(secondfile,'r')

    # printing the content of file before appending
    print("content of first file before appending:",f1.read())
    print("content of second file before appending:", f2.read())

    #closeing file
    f1.close()
    f1.close()

    #opening first file in append mode
    f1 = open(firstfile,'a+')
    f2 = open(secondfile,'r')

    f1.write(f2.read())

    f1.seek(0)
    f2.seek(0)
    print("content of first file after appending:",f1.read())
    print("content of second file after appending:", f2.read())

    # closeing file
    f1.close()
    f1.close()