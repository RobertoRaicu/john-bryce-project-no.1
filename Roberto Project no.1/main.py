import helper
import os
import sys

def main():
    books = {}
    customers = {}
    main_id = 1
    books, customers, main_id = helper.read()
    print("welcome to my library!\nfor list of comands type \"commands\" .")
    while True:
        print(customers)
        command_input = input("")
        if command_input in helper.command_names:
            os.system('cls' if os.name == 'nt' else 'clear')
            if command_input == "commands":
                print(*helper.command_names, sep=", ")
            elif command_input == "exit":
                helper.save(books,customers, main_id)
                sys.exit("good bye!")
            else:
                helper.execute_command(command_input,customers,books,main_id)
                if command_input == "add_customer":
                    print(f"new customer's id is: {main_id}")
                    main_id += 1
                print("for list of comands type \"commands\" .")
        else:
            print("invalid command\nfor list of comands type \"commands\" .")

if __name__ == "__main__":
    main()
