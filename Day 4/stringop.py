
# Set operations
def stringop():
    print("String operation")

    name = "Challenge"
    newName = "days"

    print(name)
    print(type(name))
    print(newName)
    print(type(name))

    # As string is array of characters we can access using subscript operatior
    print(name[0])
#    print(name[9])
    #print(name[10])  index out of bound error

    # Negativ index access elements from right to left

    print(name[-1])
    print(name[-2])
    print(name[-3])

    # we can also print character in range
    print(name[0:3])
    print(name[1:3])
    print(name[2:])
    print(name[:3])

    # We can also used length function to calculate a string
    print(len(name))

    # strip method removes whitespaces from beginning and end ]
    strName = "   I am performing python code     "
    print(strName.strip())

    # By using split function we can tokanize a string
    lang = "PYTHON,C,CPP,Java"
    print(lang.split(","))