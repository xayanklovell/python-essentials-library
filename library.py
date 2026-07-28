#Library Management System
#Xayan Kyle Lovell
#Python Essentials 1

# Returns (total_copies, copies_available) across the whole library as a tuple
def library_totals(books):
    pass


# Returns the book ID of the most-borrowed book, or None if no books
def most_borrowed(books):
    pass


# Asks for a number of copies, validates with try-except, returns int or None
def read_valid_copies():
    while True:
        try:
            copies = int(input("Enter the number of copies: "))
            if copies <= 0:
                print("Copies must be greater than 0.")
            else:
                return copies
        except ValueError:
            print("Invalid number. Please enter a whole number.")

    
#Adds a new book OR adds copies to an existing title by the same author
def add_book(books):
    global next_book_number
    title = input("Enter the book title: ")
    author = input ("Enter the author: ")
    copies = read_valid_copies()

    #Searches for every existing book first
    for book_id in books:
        book = books[book_id]
        if book ["title"] == title and book["author"] == author:
            if book["title"] == title and book["author"] == author:
                book["total"] = book["total"] + copies
                book["available"] = book["available"] + copies
            print("Book already exist! Copies have been updated.")
            return

    #If we never found the book create a brand new one 
    book_id = "B" + str(next_book_number)
    books[book_id] = {
        "title": title,
        "author": author,
        "total": copies,
        "available": copies,
        "times_borrowed": 0
    }
    next_book_number = next_book_number + 1
    print("New book added!")
    print(books)

    
# Registers a new member with an empty borrowed list
def register_member(members):
    global next_member_number


# One member borrows one book - enforces ALL the rules, updates BOTH dicts
def borrow_book(books, members):
    pass


# One member returns one book - updates BOTH dicts
def return_book(books, members):
    pass


# Case-insensitive keyword search over titles
def search_catalogue(books):
    pass


# Prints one member with the TITLES of their borrowed books
def member_summary(books, members):
    pass


# Prints the whole-library report
def library_report(books, members):
    pass


# ---- Main Program ----

books = {}
members = {}
next_book_number = 1
next_member_number = 1

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add a book")
    print("2. Register a member")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Search the catalogue")
    print("6. Member summary")
    print("7. Library report")
    print("8. Exit")
    choice = input("\nChose an option(1-8): ")
    if choice == "1":
        add_book(books)
    elif choice == "8":
        print("Goodbye!")
        break
    else:
        print("Feature coming soon!")
    