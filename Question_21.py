#21. Make a Custom Class Iterable
#Assignment:
#Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

class Countdown:
    def _init_(self, start):
        self.current = start

    def _iter_(self):
        return self  

    def _next_(self):
        if self.current < 0:
            raise StopIteration
        else:
            val = self.current
            self.current -= 1
            return val
        
for num in Countdown(5):
    print(num)