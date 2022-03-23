import json

class customer:

    def __init__(self,id,name,city,age,customer_loans):
        self.id = id
        self.name = name
        self.city = city
        self.age = age
        self.customer_loans = customer_loans
        self.penalty_date = None
        self.has_returned_late = False

def add_customer(customers,main_id):
    id = str(main_id)
    name = input("last + first name: ")
    city = input("city of residence: ")
    age = input("age of customer: ")
    customer_loans = []

    customers[str(id)] = customer(id,name,city,age,customer_loans)

def display_all_customers(customers):
    print(f"there are {len(customers)} members to this library")
    print (" , ".join([str(person) for person in customers.keys()]))

def find_customer_by_id(customers):
    id_input = input("enter customer ID: ")
    if not id_input in customers.keys():
        print("no customer with that id")
        return
    
    print(id_input)
    print(f"name of customer: {customers[id_input].name}, city of residence: {customers[id_input].city}, age of customer: {customers[id_input].age}")

def remove_customer(customers):
    customer_id = input("id of customer you wish to remove (disclaimer! this change is permanent!): ")

    if not customer_id in customers:
        print("no customer with that id")
        return

    if len(customers[customer_id].customer_loans) == 0:
        del(customers[customer_id])
    else:
        print("cannot remove customer! customer has yet to turn in all his loaned books")