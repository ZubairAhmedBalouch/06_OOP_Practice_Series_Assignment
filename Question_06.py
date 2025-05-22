#6. Constructors and Destructors
#Assignment:
#Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class Logger():
    def _init_(self):
        print("Logger object created.")
        
    def _del_(self):
        print("Logger object destroyed.")    
        
obj1 = Logger()
del obj1