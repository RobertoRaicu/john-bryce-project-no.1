import datetime
today = datetime.date.today()

class loan:
    def __init__(self,customer_id,book_name,loan_date,return_date):
        self.customer_id = customer_id
        self.book_name = book_name
        self.loan_date = loan_date
        self.return_date = return_date
        
def loan_book(books,customers):
    customer_id = input("customer's id: ")

    if not customer_id in customers:
        print("no customer with that id")
        return

    if len(customers[customer_id].customer_loans) == 3:
        print("sorry you've reached the max amount of of books you can loan")
        return

    for customer_loan in customers[customer_id].customer_loans:
        if customer_loan.return_date < today:
            print("cannot loan, late due on another loan")
            return

    if customers[customer_id].has_returned_late == True:
        penalty_end = customers[customer_id].penalty_date + datetime.timedelta(days=14)
        if today < penalty_end:
            print(f"penatly still ongoing for not truning in book in time, {(penalty_end - today).days} days left")
            return
    
    book_name = input("name of book being loaned: ")
    loan_date = today 

    while not (book_name in books):
        print("book not in library")
        book_name = input("name of book: ")

    if books[book_name].num_of_copies == 0:
        print("sorry, all copies if that book are being lent right now.")
        return
    else:
        books[book_name].num_of_copies -= 1
    
    if books[book_name].type == 1:
        return_date = loan_date + datetime.timedelta(days=10)
    elif books[book_name].type == 2:
        return_date = loan_date + datetime.timedelta(days=5)
    else:
        return_date = loan_date + datetime.timedelta(days=2)
    
    #to test late loans related funtions replace line bellow with : customers[customer_id].customer_loans.append(loan(customer_id,book_name, loan_date, return_date - datetime.timedelta(days=14)))
    customers[customer_id].customer_loans.append(loan(customer_id,book_name, loan_date, return_date))
    print("book successfully loaned")

def return_book(customers,books):
    customer_id = input("customer's id: ")

    if not customer_id in customers:
        print("no customer with that id")
        return

    book_name_input = input("name of book: ")

    if not book_name_input in books.keys():
        print("book not in library")
        return

    for borrow in customers[customer_id].customer_loans:
        if borrow.book_name == book_name_input:
            if borrow.return_date < today:
                print("you have return this book late. you will not be able to loan a book for the next two weeks :(")
                customers[customer_id].penalty_date = today
                customers[customer_id].has_returned_late = True
    
    has_loaned = False
    
    for i, loan in enumerate(customers[customer_id].customer_loans):
        if book_name_input == loan.book_name:
            has_loaned = True
            del(customers[customer_id].customer_loans[i])

    if not has_loaned:
        print("sorry you have not loaned this book")
        return
    
    books[book_name_input].num_of_copies += 1

def display_all_loans(customers):
    for person in customers.values():
        for borrow in person.customer_loans:
            print(f"name of borrower: {person.name}#{borrow.customer_id}, name of borrowed book: {borrow.book_name}, loan date: {borrow.loan_date}, return date due: {borrow.return_date}")

def display_late_loans(customers):
    has_late_loans = False
    for person in customers.values():
        for borrow in person.customer_loans:
            if borrow.return_date < today:
                print(f"name of borrower: {person.name}#{borrow.customer_id}, name of borrowed book: {borrow.book_name}, loan date: {borrow.loan_date}, return date due: {borrow.return_date}")
                has_late_loans = True
    if not has_late_loans:
        print("no late loans")

def display_loans_by_costumer(customers):
    customer_id = input("customer's id: ")
    if not customer_id in customers:
        print("no customer with that id")
        return

    for loans in customers[customer_id].customer_loans:
        print(f"name of borrowed book: {loans.book_name}, loan date: {loans.loan_date}, return date due: {loans.return_date}")

def display_loans_by_book(books,customers):
    book_input = input("name of book: ")
    if not book_input in books:
        print("book not in library")
        return

    for person in customers.values():
        for borrow in person.customer_loans:
            if book_input == borrow.book_name:
                print(f"name of borrower: {person.name}#{borrow.customer_id}, loan date: {borrow.loan_date}, return date due: {borrow.return_date}")



    





