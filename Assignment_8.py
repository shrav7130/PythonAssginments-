# Shravan Surve

class A:
    def __init__(self,a,b,c):
        self.__a=a
        self._b=b
        self.c=c

    def display(self):
        print("Class A:")
        print("Value of a:",self.__a)
        print("Value of b:",self._b)
        print("value of c:",self.c)

class B(A):
    def display(self):
        try:
            print("Class B:")
            print("Value of a:",self.__a)
        except AttributeError:
            print("Accessing private member a in class B is not allowed ")
        print("Value of b:",self._b)
        print("value of c:",self.c)


obj1=B(40,55,32)
obj1.display()

