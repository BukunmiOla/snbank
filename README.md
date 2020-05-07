# snbank
A basic banking system that stores data using the Python File System

##### Background:
Having created the project folder, new files (staff.txt and customer.txt) were added to the project.
The staff.txt contains 2 staff details which had their Username, Password, Email andFull Name
While customer.txt remained empty
The flowchart of how the program run is given below.
![flowchart](/flowchart.jpg)
##### Data used:
* Username (string)
* Password (string)
* Account name (string)
* Opening Balance (Float)
* Account type (string)
* Account email (string)
* Account number (string)

###### Libraries used:
* os
* random

##### Functions:
* staff_login():
* create_account(username)
* check_email(account_email)
* generate_account_number()
* fetch_account(account_number,username)

Implementation:

On run, what the program does is to present the following to the user:

1. Staff Login
1. Close App

> If the user selects *Login*, the program prompts the user to enter username and password.
> The program then checks through the staff.txt file and verify that the username and password are correct.
> If incorrect, the program prints "Invalid credentials, try again!"
> The program then goes back to the staff login page
> Once user login is successful, a new file named user_session.txt is created in the project directory to store the user session (login details, created accounts and checked account with their timestamp).
> All these are handled by the staff_login() function.

> Also, the staff is presented with the following options: 

1. Create new bank account

1. Check Account Details

1. Logout


* If staff selects Create bank account, the create_account(username) function starts working, so the program prompts the staff to supply the following:
> Account name, Opening Balance, Account Type and Account email
> When email is supplied, the check_email(account_email) function validates the email.
> If email is not valid, the program prints "Invalid email! Try again!".
> After all fields has been supplied, the generate_account_number() function generates random 9 digits and join it to 2 being the Identity I chose.

> When staff completes creating the account, the generated account number is displayed and the details are appended to the customer.txt file. And also append the created account number and timestamp to the user_session.txt file.
 
* If Staff selects check account details, the program request for account number which is taken by the fetch_account(account_number, username) function

> The program then fetch the details of the account from the customer.txt file and display it to the staff, the checked account number and timestamp is appended to there user_session.txt file as well.

After each process, the staff is presented with the options again.

* If staff selects logout, the user_session.txt file is deleted and the program returns to the staff login page.

 
* Finally, if staff selects Close App, the program terminates.
