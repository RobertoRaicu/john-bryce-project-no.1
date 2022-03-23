import json

class book:

    num_of_copies_total = 1
    num_of_copies = 1

    def __init__(self,name,author,year_published,type):
        self.name = name
        self.author = author
        self.year_published = year_published
        self.type = type
    
def add_book(books):
    name = input("title of book: ")
    if name in books.keys():
        books[name].num_of_copies_total += 1
        books[name].num_of_copies += 1
        print("book already in library. new coppy added!")
        return
    
    author = input("name of author: ")
    year_published = input("year published: ")

    while True:
        type = input("numeric type\n(type 1: loan up to 10 days, 2: up to 5 days, 3: up to 2 days)\n: ")
        if type == "1" or type == "2" or type == "3":
            type = int(type)
            break
        else:
            print("invalid input")

    books[name] = book(name, author, year_published, type)

def display_all_books(books):

    print(f"there are {len(books)} uniqe books in the library at the momemt")
    print (" , ".join([str(i) for i in books.keys()]))

def find_book_by_name(books):
    book_name = input("name of book: ")

    if not book_name in books.keys():
        print("book not in library")
        return

    print(f"title of book: {books[book_name].name}, author of book: {books[book_name].author}, year published: {books[book_name].year_published}, borrowing time type: {books[book_name].type}, no. of copies in library: {books[book_name].num_of_copies}")
       
def remove_book(books):
    book_name = input("name of book you wish to remove (disclaimer! this change is permanent!): ")

    if not book_name in books.keys():
        print("book not in library")
        return
    
    if books[book_name].num_of_copies_total == books[book_name].num_of_copies:
        del(books[book_name])
        print("book removed successfuly")
    else:
        print("cannot remove book! not all copies of this book have been returned to the library.")
