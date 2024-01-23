

def area():

    redius= int(input("Enter a redius of a circle:"))

    area=calarea(redius)
    print("area of a circle",area)


def calarea(redius):
    pi=3.14
    area = 3.14 * redius * redius;
    return area;

