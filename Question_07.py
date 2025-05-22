#7. Access Modifiers: Public, Private, and Protected
#Assignment:
#Create a class Employee with:
    #a public variable name,
    #a protected variable _salary, and
    #a private variable __ssn.
    #Try accessing all three variables from an object of the class and document what happens.


class Employee:
    def _init_(self, name, salary, ssn ):
        self.name = name
        self.salary = salary
        self.__ssn = ssn

emp = Employee("Ramiz Raja", 11000, 123)
print(emp.name)
print(emp.salary)
print(emp.__ssn)