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
    pass


# Adds a new book OR adds copies to an existing title by the same author
def add_book(books):
    pass


# Registers a new member with an empty borrowed list
def register_member(members):
    pass


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
    break