#13. Composition
#Assignment:
#Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.


class Engine:
    
    def start_engine(self):
        print("Engine started...")
        
class Car:
    def _init_(self, engine):
        self.engine = engine
        
    def start_car(self):
        self.engine.start_engine()
        print("Car started...")
        
car_engine = Engine()

car = Car(car_engine)

car.start_car()