#11. Class Methods
#Assignment:
#Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.


class Book:
    total_books = 0
    
    def _init_(self, title):
        self.title = title
        Book.increment_book_count()
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books +=1
        
book1 = Book("Python Programming")
book2 = Book("Data Science")
book3 = Book("Machine Learning")        
        
print("Total books: ", Book.total_books) 