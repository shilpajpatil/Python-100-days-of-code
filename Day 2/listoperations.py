

def listoperations():
    print("list operations ")
    # Create an empty list
    list1 = [23,56,89,54,"max"]
    """
    # add elements inside list
    for i in range(5):
        num = int(input("enter items to add inside the list"))
        list1.append(num)
    """
    # print the list with updated items
    print(list1)

    #Append an string into list
    list1.append("Hello")
    print("Result of appent operation:",list1)

    # by using remove we can remove element from list
    list1.remove("Hello")
    print("Result of remove operation", list1)
    #insert , is used to add item at perticular index
    list1.insert(3,"good")
    print("result of insert operation:",list1)

    #by using remove we can remove element from list
    list1.remove("max")
    print("Result of remove operation",list1)

    #pop function in list
    list1.pop()
    print("Result of pop operation:",list1)

    del list1[1:]
    print("after del operation performed:", list1)

    list1.extend([134,"Hello",89,"mylist"])
    print("Extended list:", list1)

    # sort operation display list in assending order
    # sort operation will not apply on hectrogenius string
    list1.sort()
    print("Sorted list:",list1)
