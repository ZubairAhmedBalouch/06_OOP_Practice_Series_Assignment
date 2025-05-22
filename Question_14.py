#14. Aggregation
#Assignment:
#Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employe:
    def _init_(self, name):
        self.name = name
        
    def get_details(self):
        return f"Employee Name: {self.name}"
      
class Department:
    def _init_(self, dept_name, employe):
        self.dept_name = dept_name
        self.employe = employe
        
    def show_employe(self):
        return f" {self.dept_name} Department has {self.employe.get_details()}"
            
            
emp1 = Employe("Fatima")
dep = Department("HR", emp1)
print(dep.show_employe())