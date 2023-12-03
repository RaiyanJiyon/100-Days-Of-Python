class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def display_books(self):
        if self.no_of_books == 0:
            print("The library is empty.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book)

    def add_book(self, book_title):
        self.books.append(book_title)
        self.no_of_books += 1
        print(f"'{book_title}' has been added to the library.")

    def get_no_of_books(self):
        return self.no_of_books

# Main program
if __name__ == "__main__":
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
            print(f"The library has {my_library.get_no_of_books()} books.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")

print("Library program has ended. Books are not persisted.")
