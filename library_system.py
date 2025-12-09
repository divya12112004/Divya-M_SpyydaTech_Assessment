# Simple Library Management System (Console Menu)

class Book:
    def __init__(self, book_id, title, author, is_borrowed=False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed


# List to store all books
books = []


def read_int(message):
    """Read an integer safely from user input."""
    try:
        value = int(input(message))
        return value
    except ValueError:
        print("Invalid number!")
        return None


def add_book():
    """Add a new book to the library."""
    book_id = read_int("Enter book ID (number): ")
    if book_id is None:
        return

    title = input("Enter book title: ").strip()
    author = input("Enter book author: ").strip()

    if not title or not author:
        print("Title and author cannot be empty.")
        return

    # Check if ID already exists
    for b in books:
        if b.book_id == book_id:
            print("A book with this ID already exists.")
            return

    new_book = Book(book_id, title, author)
    books.append(new_book)
    print("Book added successfully!")


def search_book():
    """Search a book by ID or part of the title."""
    query = input("Enter book ID or part of title to search: ").strip()

    if not query:
        print("Search text cannot be empty.")
        return

    found = False
    query_lower = query.lower()

    for b in books:
        if str(b.book_id) == query or query_lower in b.title.lower():
            print("-" * 30)
            print(f"ID     : {b.book_id}")
            print(f"Title  : {b.title}")
            print(f"Author : {b.author}")
            print(f"Status : {'Borrowed' if b.is_borrowed else 'Available'}")
            found = True

    if not found:
        print("No matching book found.")


def borrow_book():
    """Borrow a book using its ID."""
    book_id = read_int("Enter book ID to borrow: ")
    if book_id is None:
        return

    for b in books:
        if b.book_id == book_id:
            if b.is_borrowed:
                print("This book is already borrowed.")
            else:
                b.is_borrowed = True
                print(f"You borrowed the book: {b.title}")
            return

    print("Book with this ID not found.")


def return_book():
    """Return a borrowed book using its ID."""
    book_id = read_int("Enter book ID to return: ")
    if book_id is None:
        return

    for b in books:
        if b.book_id == book_id:
            if not b.is_borrowed:
                print("This book was not borrowed.")
            else:
                b.is_borrowed = False
                print(f"You returned the book: {b.title}")
            return

    print("Book with this ID not found.")


def show_all_books():
    """Display all books in the library."""
    if not books:
        print("No books in the library yet.")
        return

    print("\nAll Books in Library:")
    for b in books:
        print("-" * 30)
        print(f"ID     : {b.book_id}")
        print(f"Title  : {b.title}")
        print(f"Author : {b.author}")
        print(f"Status : {'Borrowed' if b.is_borrowed else 'Available'}")


def main():
    while True:
        print("\n=== Library Management System ===")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Show All Books")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            search_book()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            show_all_books()
        elif choice == "0":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
