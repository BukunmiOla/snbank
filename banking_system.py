#import libraries
import os
import random
import datetime 


#Variables declaration
username = ""
password = ""
full_name = ""
account_name = ""
account_number = ""
account_type = ""
account_email = ""
opening_balance = 0.00

#Functions : staff_login, create_account, check_email, generate_account_number fetch_account and main

#This fiunction processes the login detail of the staff
def staff_login():
    user_exist= False
    username = input("Enter username here : ")
    password = input("Enter password here : ")
    staff = open("staff.txt", "r")
    check =staff.readlines()
    detail = username+":"+password
    for x in check :
        yes= detail in str(x)
        if yes == True:
           user_exist = True
    staff.close()
    if user_exist:
        print("Login successful")
        user_session = open("user_session.txt", "w")
        user_session.write(username+" logged in successfully at ")
        user_session.write(str(datetime.datetime.now())) # prints the current date and time in the file
        user_session.close()
    else:
        print ("User details does not exit")
    return user_exist

# This function creates account for the customers taking their names, account type, email opening balance and then supply their account numbers
def create_account ():
    account_name = input ("Enter account name : ")
    account_email = input ("Enter account email : ")
    correct_email = check_email(account_email)          #jump to the function check_email()
    while correct_email==False:
        print ("The email address you entered is INVALID! Please try again.")
        account_email = input("\nEnter email here: ")
        correct_email = check_email(account_email)
        
    print ("Select account type. \n1. Current \n2. Savings \n3. Fixed")
    _type = input(">>")
    if _type == "1":
        account_type = "Current"
    elif _type == "2":
        account_type = "Savings"
    elif _type == "3":
        account_type = "Fixed"
    opening_balance = float(input("Enter opening balance : "))
    account_number = generate_account_number()
    customers = open("customer.txt", "a")
    account_details = "\n"+account_name+" ; "+account_number+" ; "+account_type+ " ; "+ account_email+ " ; "+ str(opening_balance)
    customers.write(account_details)
    print("Account created successfully")
    customers.close()

    user_session = open("user_session.txt", "a")
    user_session.write("\n   created account "+account_number+" at ")
    user_session.write(str(datetime.datetime.now())) # prints the current time in the file
    user_session.close()
    

    return account_number

#This function checks the validity of the email supplied 
def check_email(email):
    
    com = email.endswith(".com") #This will check if the email ends with .com
    at = '@' in email            #this will check if the email contains the character @
    
    if com == True and at == True:
        correct_email=True
    else:
        correct_email=False
        
    return correct_email
    
#This function generates account number for the customer such that every account number starts with 2
def generate_account_number():
    generate=True
    while generate:
        account_number = "2"+''.join(random.choice("0123456789")for i in range(9))
        customer = open("customer.txt", "r")
        check =customer.readlines()
        for x in check :
            yes= account_number in str(x)
            if yes == True:
                generate = True
            else:
                generate = False
    else:
        print ("Account number is ", account_number)
    

    return account_number
    
#This function will fetch the account details of a customer whose account number has been supplied from the text file
def fetch_account(account_number):
    customers = open("customer.txt", "r")
    fetching =customers.readlines()
    for x in fetching:
        yes = account_number in str(x)
        if  yes:
            print("Find account details below. \naccount_name ; account_number ; account_type ;  account_email ; opening_balance")
            print(x)

    user_session = open("user_session.txt", "a")
    user_session.write("\n   checked account details of "+account_number+" at ")
    user_session.write(str(datetime.datetime.now())) # prints the current time in the file
    user_session.close()

#This is the main function
def main():
    print("Hello, Good day! \nWelcome to StartNg Bank Plc.")
    action = input("Enter 1 to Login or any other key to Close App >")
    while action == "1":
        user_exist=staff_login()
        
        while user_exist==True:
            action=""
            print("What would you like to do? Enter 1,2 or 3.")
            action = input("1. Create new Account. \n2. Check Account details. \n3. Log Out \n>>")
            if action == "1":
                create_account()
            elif action == "2":
                account_number = input("Enter account number here: ")
                fetch_account(account_number)
            elif action == "3":
                os.remove("user_session.txt")
                user_exist = False
                main()
            else:
                print ("Invalid input! Please enter a valid input")

        else: 
            print("No User is logged in")
            main()


    else:
        exit()
main()