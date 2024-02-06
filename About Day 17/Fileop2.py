

# Reading a file character by character


def fileread2():
    file = open('About Day 17.txt', 'r')

    while 1:
        char = file.read(1)
        if not char:
            break
        print(char)


    file.close