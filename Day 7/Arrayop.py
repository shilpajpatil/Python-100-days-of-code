

import array as arr
# Set operations
def arrayop():

    # As there is no direct support for array so we need to import  array

    a = arr.array('i',[2,4,6,8])

    print("First elelment:",a[0])
    print("Second element",a[1])
    print("second last element",a[-1])

    array2=arr.array('f',[2.4,4.5,6,5,8.8])


    print("First elelment:",array2[0])
    print("Second element",array2[1])
    print("second last element",array2[-1])

    print(array2.typecode)
    array2.reverse()

    for i in range(len(a)):
        print(a[i])
