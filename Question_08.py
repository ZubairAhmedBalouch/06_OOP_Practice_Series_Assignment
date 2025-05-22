#8. The super() Function
#Assignment:
#Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

class Person():
    def _init_(self, name):
        self.name = name

class Teacher(Person):
    def _init_(self, name, subject):
        super()._init_(name) 
        self.subject = subject
        
teacher = Teacher("Ramiz Raja", "Math")
print(teacher.name)
print(teacher.subject) 