#3. Public Variables and Methods
#Assignment:
#Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    def _init_(self, brand):
        self.brand = brand
        
    def start(self):
        print("Car started...")
        
car1 = Car("Toyota")
print(car1.brand)
car1.start()  