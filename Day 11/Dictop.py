

# Dictoinary operations

# Dictionary stores data values in key value pair
def dictop():

# convert two list into dictionaries
    key= [1,2,3,4,5]
    value = ['One','Two','Three','Four','Five']
    d1 = dict(zip(key,value))
    print("d1 dict:",d1)


# Add two dictionaries in one
    d2 = {1:100,2:200,3:300}

    dict3 = {**d1,**d2}
    print("added two dict", dict3)