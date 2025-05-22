#19. callable() and __call__()
#Assignment:
#Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.

class Multiplier:
    def _init_(self, factor):
        self.factor = factor

    def _call_(self, number):
        return self.factor * number

m = Multiplier(3)


print(m(5))          

print(callable(m))   
