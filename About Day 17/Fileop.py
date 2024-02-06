

# Read a file word by word

def fileread():


    with open('About Day 17.txt', 'r') as file:
        for line in file:
            for word in line.split():
                print(word)