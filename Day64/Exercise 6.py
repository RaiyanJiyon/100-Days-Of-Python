'''Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the books after the program is stopped!'''

class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def display_books(self):
        if self.no_of_books == 0:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book)

    def add_book(self, book_title):
        self.books.append(book_title)
        print(f"{book_title} book is added to the library.")
        self.no_of_books += 1

    def get_books_count(self):
        return self.no_of_books

# Main Program
if __name__ == "__main":
    my_library = Library()

    while True:
        print("\nLibrary Menu:")
        print("1. Display all books")
        print("2. Add a book")
        print("3. Get the number of books")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            my_library.display_books()
        elif choice == "2":
            book_title = input("Enter the title of the book: ")
            my_library.add_book(book_title)
        elif choice == "3":
            print(f"Currently, there are {my_library.get_books_count()} books available.")
        elif choice == "4":
            break
        else:
            print("Invalid Input. Please enter between (1/2/3/4):")

    print("Library program has ended. Books are not persisted.")


         

         


    

      