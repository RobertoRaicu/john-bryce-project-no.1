![logo](https://www.johnbryce.co.il/src/jbh_small.jpg)

# john bryce 7731/5 project no.1

submited by: Roberto Raicu

> ### **this is a simple sorting system meant for the staff₁ of a public library which allows you to manage the entirety of the system**
>
> ---
>
> - add a customer
>   - saves customer's details alongside an ID
>   - to add customer use command: `add_customer`
>   - to remove customer use command: `remove_customer`
>       - _customer may be removed only if they have no active loans_
>   - to see customer's info use command: `find_customer_by_id`
>   - to see list of all customers use command: `display_all_customers`
>
> ---
>
> - add a book
>   - saves book's details\*:
>     - \*every book has a numeric type:
>       1. loan book for up to 10 days
>       2. loan book for up to 5 days
>       3. loan book for up to 2 days
>   - to add book use command: `add_book`
>   - to remove book use command: `remove_book`
>     - _book may be removed only if all copies are present in the library and not loaned_
>   - to see book's info use command: `find_book_by_name`
>   - to see list of all books use command: `display_all_books`
>
> ---
>
> - loan a book
>   - to loans a book use command `loan_book`
>     - _customer may not loan a book if they have a "late loan" pentaly ongoing_
>   - keeps track of loans of customers
>     - use command: `display_book_by_costumer`
>   - keeps tracks of loan date and late due
>     - use command: `display_late_loans`
>   - keep tracks of multiple book copies loaned
>     - use command: `display_book_by_loan`
>   - to display all loans collectively use command: `display_all_loans`
>
> ---
>
> - return a book
>   - to return a book use command `return_book`
>   - if customer returns book past the return date, they will automatically recieve a penalty of two weeks in which they cannot loan a new book
>
> ---
>
> - save
>   - all data is being saved automatically onto `savefile.json` file uppon termination of the program
>   - to terminate program use command: `exit`
>   - to save without termination at any point use command: `save`
>   - if the upload save funtion, `helper.read()`, is not called automatically on startup for some reason.  
>      the command: `upload_save` , is available.
>
> ---
>
> ## **!! disclaimers !!** :
>
> - **save file shall always be named "`savefile.json`"**
> - **an empty savefile shall always contain "`{}`" at the beginning of the file**
>   - otherwise `helper.read()` will return an error
> - **program shall be terminated by using command `exit` first**
>   - this program runs on the terminal! due to that fact, terminating the terminal before terminating the program itself via `exit` will result in the program not saving your new inputs/data!!

##### 1. because of the limited time for this due, not all open texts check for correct input and therefore assumes correct use.

&nbsp;

&nbsp;

> Raicu Roberto  
> RobertoMeer123@gmail.com  
> john bryce 7731/5
