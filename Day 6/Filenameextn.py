
# write a python program and accept a filename from user and print extension

def extn():
    filename = input("Enter a file name:")

    f_extn = filename.split(".")

    print("The extension of file is:",  repr(f_extn[-1]))