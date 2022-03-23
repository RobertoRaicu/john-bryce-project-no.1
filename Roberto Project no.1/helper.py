import Customers
import Books
import Loans
import json
import datetime

command_names = ["add_customer", "add_book", "loan_book", "return_book", "display_all_books", "display_all_customers", "display_all_loans", "display_late_loans", "display_loans_by_customer", "display_loans_by_book", "find_book_by_name", "find_customer_by_id", "remove_book", "remove_customer", "commands", "save", "upload_save", "exit"]

def save(books,customers, main_id):
            dict_to_save = {"list_of_customers": [],
                "list_of_books": [],
                "main_id": main_id}
            for cust in customers.values():
                customer_dictionary = cust.__dict__.copy()
                customer_loans = []
                for cust_loan in customer_dictionary['customer_loans']:
                    loan_dict = cust_loan.__dict__.copy()
                    loan_dict["loan_date"] = str(loan_dict["loan_date"])
                    loan_dict["return_date"] = str(loan_dict["return_date"])  

                    customer_loans.append(loan_dict)

                customer_dictionary['penalty_date'] = str(customer_dictionary['penalty_date'])    
                customer_dictionary['customer_loans'] = customer_loans
                
                dict_to_save['list_of_customers'].append(customer_dictionary)

            for bo in books.values():
                book_dict = bo.__dict__
                book_dict["num_of_copies"] = bo.num_of_copies
                book_dict["num_of_copies_total"] = bo.num_of_copies_total
                dict_to_save["list_of_books"].append(book_dict)


            with open('savefile.json', 'w') as json_file:
                json.dump(dict_to_save, json_file, indent=2)

def read():
    data = None
    with open('savefile.json', 'r') as json_file:
        data = json.load(json_file)

    books = {}
    customers = {}

    if len(data.values()) == 0:
        return books, customers, 1

    main_id = data["main_id"]

    for book_dict in data["list_of_books"]:
        book_name = book_dict["name"]
        book_author = book_dict["author"]
        book_year_published = book_dict["year_published"]
        book_type = book_dict["type"]
        book_copies = book_dict["num_of_copies"]
        book_copies_total = book_dict["num_of_copies_total"]
        books[book_name] = Books.book(book_name, book_author, book_year_published, book_type)
        books[book_name].num_of_copies = book_copies
        books[book_name].num_of_copies_total = book_copies_total

    for person in data["list_of_customers"]:
        person_id = person["id"]
        person_name = person["name"]
        person_city = person["city"]
        person_age = person["age"]
        person_loans = []

        for loan in person["customer_loans"]:
            loan_id = loan["customer_id"]
            loan_book = loan["book_name"]
            ld = datetime.datetime.strptime(loan["loan_date"],"%Y-%m-%d")
            loan_date = ld.date()
            rd = datetime.datetime.strptime(loan["return_date"],"%Y-%m-%d")
            loan_return = rd.date()
            person_loans.append(Loans.loan(loan_id, loan_book, loan_date, loan_return))
    
        person_penalty = person['penalty_date']
        if person_penalty != "None":
            person_penalty = datetime.datetime.strptime(person["penalty_date"],"%Y-%m-%d")
        else:
            person_penalty = None
    
        person_late = person["has_returned_late"]
    
        customers[person_id] = Customers.customer(person_id, person_name, person_city, person_age, person_loans)
        customers[person_id].penalty_date = person_penalty
        customers[person_id].has_returned_late = person_late
        
    return books, customers, main_id   

def execute_command(command_input,customers,books,main_id):
    if command_input == "add_customer":
        Customers.add_customer(customers,main_id)

    elif command_input == "add_book":
        Books.add_book(books)

    elif command_input == "loan_book":
        Loans.loan_book(books,customers)

    elif command_input == "return_book":
        Loans.return_book(customers,books)

    elif command_input == "display_all_books":
        Books.display_all_books(books)

    elif command_input == "display_all_customers":
        Customers.display_all_customers(customers)

    elif command_input == "display_all_loans":
        Loans.display_all_loans(customers)

    elif command_input == "display_late_loans":
        Loans.display_late_loans(customers)

    elif command_input == "display_loans_by_customer":
        Loans.display_loans_by_costumer(customers)

    elif command_input == "display_loans_by_book":
        Loans.display_loans_by_book(books,customers)

    elif command_input == "find_book_by_name":
        Books.find_book_by_name(books)

    elif command_input == "find_customer_by_id":
        Customers.find_customer_by_id(customers)

    elif command_input == "remove_book":
        Books.remove_book(books)

    elif command_input == "remove_customer":
        Customers.remove_customer(customers)

    if command_input == "save":           
        save(books,customers, main_id)
    
    if command_input == "upload_save":
        read()
        print("save uploaded")
            
    
