
# Set operations
def setoperations():
    myset = {11,'python', 54,'ML'}

    print("User set is:", myset)


    # Set has no attribute append, insert
    myset.remove(54)
    print(myset)

    myset.discard('ML')
    print(myset)

    myset.add('OOP')
    print(myset)