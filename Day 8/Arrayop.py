

from  array import *
# Set operations
def arrayop():

    # As there is no direct support for array so we need to import  array

    a = array('i',[2,4,6,8,2,5,2,5])


    print(str(a));

    a.append(12)
    print(a)
    print(len(a))

    print(a.buffer_info())
   # print(a.buffer_info()[1]* a.itemssize)

    num = int(input("Enter a number to check occurence of that numebr:"))
    print(a.count(num))

    a.remove(num)
    print(a)