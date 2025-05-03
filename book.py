# 11. Class Methods
#Assignment:
#Create a class Book with a class variable total_books. 
# Add a class method increment_book_count() 
# to increase the count when a new book is added.

# Python Code: 
# Book Class with Class Method and Class Variable

class Book:
    total_books = 0
    all_titles = []
    all_authors = []

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()
        Book.all_titles.append(self.title)
        Book.all_authors.append(self.author)

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        print(f"NewBook added. Total books: {cls.total_books}")

    
    @classmethod
    def reset_book_count(cls):
        cls.total_books = 0
        cls.all_titles.clear()
        cls.all_authors.clear()
        print("Book count reset to zero.")
    
    @classmethod
    def show_all_titles(cls):
        print("\n--- All  Book Titles ---")
        if not cls.all_titles:
            print("No books in the library.")
        else:
            for title in cls.all_titles:
                print(f" - {title}")
    
    @classmethod
    def show_all_authors(cls):
        print("\n--- All  Book Authors ---")
        if not cls.all_authors:
            print("No authors in the library.")
        else:
            for author in cls.all_authors:
                print(f" - {author}")

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}")


# Creating Book objects
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")
book4 = Book("The Hobbit", "J.R.R. Tolkien")
book5 = Book("Frankenstein", "Mary Shelley")

# Displaying book details
book1.display()
book2.display()
book3.display()
book4.display()
book5.display()

# Show all titles and total
Book.show_all_titles()
Book.show_all_authors()
print("\nTotal books in library:",Book.total_books)

# For Reset book count
# Book.reset_book_count()
# Book.show_all_titles()
# print("\nTotal books in library:",Book.total_books)


              