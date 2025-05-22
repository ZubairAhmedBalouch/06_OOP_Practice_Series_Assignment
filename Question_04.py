#4. Class Variables and Class Methods
#Assignment:
#Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "ABC Bank"
    
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
        
        
name1 = Bank()
print("Old Bank Name: ", name1.bank_name)
name1.change_bank_name("XYZ bank")  
print("New Bank Name: ", name1.bank_name)