

# Dictoinary operations

# Dictionary stores data values in key value pair
def dictop():

# Declared a dictionary
    thisdict = {
        "brand":"Oneplus",
        "Model": "Nord",
        "year": 2020
    }

    print(thisdict)
#how to access the element from dictionary using key
# for using get() we can access the value

    x= thisdict["Model"]
    print("displauing model value:",x)

    key = thisdict.keys()
    print("printing keys from dict:",key)

# Adding element in privious created list
    thisdict["color"]="Black"
    print("New dictionary:",thisdict)

#values() return list of values returned
    print("printing all values:",thisdict.values())

# changinch value from privious list
    thisdict["color"]="powderblue"
    print("printing updated list:",thisdict)


# items() -display all items in the form of tupple

    print("items() will return :",thisdict.items())
# pop()
    print("pop() will return:",thisdict.pop("color"))
    print(thisdict)

#del()
    del thisdict["Model"]
    print("After deleting model",thisdict)

# clear()  empty the dictionary



