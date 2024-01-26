

# Class in python
def dictop():
    class Demo:

        def __init__(self):
            self.i = 0
            self.j = 0

        def first(self):
            print("Inside first function")

        @classmethod
        def second(cls):
            print("Inside second class")

        @staticmethod
        def third():
            print("Inside third which is static method")


    obj1 = Demo()
    obj1.first()
    Demo.second()
    Demo.third()

