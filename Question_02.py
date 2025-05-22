#2. Using cls
#Assignment:
#Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0
    
    def _init_(self):
        Counter.count += 1
        
    @classmethod
    def get_count(cls):
        return cls.count    
    
c1 = Counter()
c2 = Counter()
c3 = Counter()
c4 = Counter()

print("Total objects created =",Counter.get_count()) 



