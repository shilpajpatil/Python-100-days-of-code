def pattern():
    rs = pattern1("Hi", 2)
    print(rs)
    rs = pattern1("Hi", 3)
    print(rs)


def pattern1(str, n):
        #  def string_times(str, n):
    result = ""
    for i in range(n):
        result = result + str

    return result


