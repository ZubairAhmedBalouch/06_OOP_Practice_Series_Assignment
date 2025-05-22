#15. Method Resolution Order (MRO) and Diamond Inheritance
#Assignment:
#Create four classes:
    #A with a method show(),
    #B and C that inherit from A and override show(),
    #D that inherits from both B and C.
    #Create an object of D and call show() to observe MRO.

class A:
    def show(self):
        print("Class A method called")
class B(A):
    def show(self):
        print("Class B method called")
class C(A):
    def show(self):
        print("Class C method called")
class D(B, C):
    def show(self):
        print("Class D method called")

d = D()
d.show()
print(D.mro())     