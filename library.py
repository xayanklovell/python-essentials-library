#Library Management System
#Xayan Kyle Lovell
#Python Essentials 1

#Prints totals for books and members in the library
def library_totals(books, members):
    total_books = 0
    available_books = 0
    borrowed_books = 0
    total_members = 0
    for book_id in books:
        book = books[book_id]
        total_books = total_books + book["total"]
        available_books = available_books + book["available"]
        borrowed_books = borrowed_books + (book["total"] - book["available"])
    for member_id in members:
        total_members = total_members + 1
    print("\n===== LIBRARY TOTALS =====")
    print("Total books:", total_books)
    print("Available books:", available_books)
    print("Borrowed books:", borrowed_books)
    print("Total members:", total_members)
    

# Returns the book ID of the most-borrowed book, or None if no books
def most_borrowed(books):
    most_book_id = None
    highest_count = -1
    for book_id in books:
        book = books[book_id]
        if book["times_borrowed"] > highest_count:
            highest_count = book["times_borrowed"]
            most_book_id = book_id
    return most_book_id
    

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
    name = input("Enter member name: ")
    if name == "":
        print("Member name cannot be blank.")
        return
    member_id = "M" + str(next_member_number)
    members[member_id] = {
    "name": name,
    "borrowed": []
    }
    next_member_number = next_member_number + 1
    print("Member " + member_id + " registered successfully!")


# One member borrows one book - enforces ALL the rules, updates BOTH dicts
def borrow_book(books, members):
    member_id = input("Enter the member ID: ")
    if member_id not in members:
        print("No such member.")
        return
    book_id = input("Enter book ID: ")
    if book_id not in books:
        print("No such book.")
        return
    if len(members[member_id]["borrowed"]) >= 3:
        print("Member has reached the borrowing limit.")
        return
    if book_id in members[member_id]["borrowed"]:
        print("Member already has this book.")
        return
    if books[book_id]["available"] == 0:
        print("No copies available.")
        return
    books[book_id]["available"] = books[book_id]["available"] - 1
    members[member_id]["borrowed"].append(book_id)
    books[book_id]["times_borrowed"] = books[book_id]["times_borrowed"] + 1
    print("Book borrowed successfully!")



# One member returns one book - updates BOTH dicts
def return_book(books, members):
    pass


# Case-insensitive keyword search over titles
def search_catalogue(books):
    keyword = input("Enter a keyword: ").lower()
    found = False
    for book_id in books:
        book = books[book_id]
        if keyword in book["title"].lower():
            print(book_id)
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Available:", book["available"], "/", book["total"])
            print()
            found = True
    if found == False:
        print("No books found.")

    
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
    elif choice == "2":
        register_member(members)
    elif choice == "3":
        borrow_book(books, members)
    elif choice == "5":
        search_catalogue(books)
    elif choice == "8":
        print("Goodbye!")
        break
    else:
        print("Feature coming soon!")
    