
import os
import random
import datetime
from datetime  import datetime

USER_FILE = "User.txt"
CUSTOMER_FILE = "Customer.txt"
ACCOUNT_FILE = "Account.txt"
TRANSACTION_HISTORY_FILE ="Transaction_History.txt"


# Create Account Function===========================================================================================

def create_account():
    print("📜======Customer Creation=====📜")
    try:
        customer_name = input("Enter your name:")
        if customer_name in USER_FILE is true:
            print(f"❌ User name already taken.Try another.")
        else:
            print(f"✅Username added successful!.")
            
    except ValueError:
        print("❌Enter the letters only!")
    customer_address = input("Enter your address:") 
    customer_phone_no = int(input("Enter your phone number:"))
    intial_balances = float(input("Enter the intial balance:$"))
    customer_NIC_no = int(input("Enter your N.I.C.No:"))
    return(customer_name,customer_address,customer_phone_no,intial_balances,customer_NIC_no)

    
    

# ============================================================================================
def file_creation():

    acc_no = auto_account_number(CUSTOMER_FILE)
    u_id = user_id(CUSTOMER_FILE)
    c_id = customer_id(CUSTOMER_FILE)

    with open("User.txt", "w") as user_info:
        user_info.write(f"{acc_no}  {u_id}   {account_creation[0]}   {account_creation[1]}   {account_creation[2]}   {account_creation[4]}\n")

    with open("Customer.txt", "w") as customer_info:
        customer_info.write(f"{acc_no}  {c_id}   {account_creation[3]}\n")

    with open ("Account.txt","w") as acconut_info:
        acconut_info.write(f"{acc_no}   {account_creation[3]} \n")

    with open("User.txt", "a") as user_info:
        user_info.write(f"{acc_no}  {u_id}   {account_creation[0]}   {account_creation[1]}   {account_creation[2]}   {account_creation[4]}\n")


    with open("Customer.txt", "a") as customer_info:
        customer_info.write(f"{acc_no}  {c_id}   {account_creation[3]}\n")

    with open ("Account.txt","a") as acconut_info:
        acconut_info.write(f"{acc_no}   {account_creation[3]} \n")
    
    # with open ("Transaction_History.txt","w") as transaction_info:
    #     transaction_info.write(f"{account_creation[]}")
    
#  Function for read file ====================================================================

# def read_user(USER_FILE):
#     accounts = {}
#     with open("User.txt", "r") as user_info:
#         for line in user_info:
#             parts = line.strip().split("  ")
#             acc_no = parts[0] 
#             initial_balances = float(parts[-1])
#             customer_name = "".join(parts[1:-1])
#             return accounts        

def read_customer():
    try:
        with open("Customer.txt", "r") as customer_info:
           lines = customer_info.readlines()
        return lines

    except FileNotFoundError:
        return[] 
        


def read_account():
    try:
        with open("Account.txt", "r") as account_info:
            lines = acconut_info.readlines()
        return lines

    except FileNotFoundError:
        return[]
        
        
# =================================================================================================================== 

    
# Fuction for Auto account number creation==========================================================================

def auto_account_number(CUSTOMER_FILE):
    return str(random.randint(1000, 9999))
    

def customer_id(CUSTOMER_FILE):
    existing = read_customer(CUSTOMER_FILE)
    return f"C_{3000 + len(existing) + 1}"
    

def user_id(CUSTOMER_FILE):
    existing = read_user(CUSTOMER_FILE)
    return f"U_{5000 + len(existing) + 1}"
    
# Banking Files====================================================================================================





# Deposit Money Function================================================================================================

def deposit_money(deposit):
    

    try:  
        
        deposit = float(input("🏧Enter amount to deposit: $"))
        if deposit > 0:
            accounts[acc_no]["balance"] += deposit
            print(f"✅Deposit successful. New balance: ${intial_balances[acc_num]:.2f}") 
        else:    
            print("❌Enter the positive numbers only!.")
            return


    except ValueError:
        print("❌Enter the numbers only!")

    with open ('CUSTOMER_FILE',"w") as customer_info:
        for acc_no in accounts.item():
            line = f"{acc_no} , {info['name']} ,{info['balance']}\n" 
            customer_info.write(line)

#============================================================================================================================

# Withdraw Money Function ====================================================================================================

def withdraw_money(withdraw): 
    try:
        amount = float(input("🏧Enter amount to withdraw: $"))
        if amount <= accounts[acc_no]["balance"]:
            accounts[acc_no]["balance"] -= amount
            print(f"✅Withdrawal successful. New balance: ${accounts[acc_no]["balance"]:.2f}")

        else:
            print("❌Insufficient funds!")

    except ValueError:
        print("❌Enter the numbers only!")

    with open ('CUSTOMER_FILE', "w") as customer_info:
        for acc_no in accounts.item():
            line = f"{acc_no} , {info['name']} ,{info['balance']}\n" 
            customer_info.write(line)


#     ==================================================


# # Check Balance Function==================================================================================================

def check_balance():
    print(f"🏧Account {create_account } Balance: ${intial_balances[selected_account]}")
    
#========================================================================================================================    


# Transaction History Function============================================================================================

def add_transaction(TRANSACTION_HISTORY_FILE, acc_number, amount, description):
    
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    transaction = f"{acc_number}, {current_time}, {amount}, {description}\n"
    
    with open("TRANSACTION_HISTORY_FILE",'a') as transaction_info:
        transaction_info.write(transaction)
    
    print("✅Transaction added successfully!")


def view_transactions(TRANSACTION_HISTORY_FILE):
    try:
        with open("TRANSACTION_HISTORY_FILE", 'r') as transaction_info:
            transactions = transaction_info.readlines()
            
            if not transactions:
                print("❌No transactions found.")
            else:
                print("📜Transaction History:")
                print("ID | Date & Time | Amount | Description")
                for transaction in transactions:
                    print(transaction.strip())
    
    except FileNotFoundError:
        print("❌Transaction history file not found")

def show_current_date():
    current_date = datetime.now().strftime("%Y-%m-%d")
    print(f"Current Date :{current_date}")


    
    
# =============================================================================================================================


#Admin Login =======================================================================

def admin_login():
    correct_admin_name = "Mary"
    correct_admin_password = "mary@123**" 
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts :
        print("📜======Admin Login======📜")
        admin_name = input("🙋 Enter the admin name:")
        admin_password = input("🙋Enter the admin password: ")
        
        if admin_name == correct_admin_name and admin_password == correct_admin_password:
            print("✅Login Success Full!")
            break

        else:         
            attempts += 1
            remaining = max_attempts - attempts
            print(f"❌Invalid Information.{remaining}attempt(s) left.")


    if attempts == max_attempts:
            print("❌Too many failed attempts.Exiting program.")
            exit()
#===================================================================================



#ATM MENU ===========================================================================
def admin_atm_menu():

    while True:

        print("🏧====ATM MENU====🏧")
        print("1.Create Account")
        print("2.Deposit Money")
        print("3.Withdraw Money")
        print("4.Check Balance")
        print("5.Transcation History")
        print("6.Exit")
        
        
        choice = input("👉Enter Your choice(1-5):")

        if choice == "1":
            account_creation = create_account()
            file_creation()
            print("✅Account Creation Success full!")
            
        elif choice == "2":
            acc_num = input("Enter your Account_no:")
            read_user(CUSTOMER_FILE)
            deposit_money(deposit)

        elif choice == "3":
            acc_num = input("Enter your Account_no:")
            read_user(CUSTOMER_FILE)
            withdraw_money(withdraw)

        elif choice == "4":
            acc_num = input("Enter your Account_no:")
            check_balance()

        elif choice =="5":
            acc_num = input("Enter your Account_no:")
            add_transaction(TRANSACTION_HISTORY_FILE, 1, 100.50, "Deposit")
            view_transactions(TRANSACTION_HISTORY_FILE)
        
        elif choice == "6":
            print("Thank you for using this mini banking system.Good bye.!😊.")
            exit()
            break

        else:
            print("❌Enter the one to six numbers only!.")


#=========================================================================================


# Users Login ==============================================================================

def users_login():
    print("📜=====Users Login======📜")
    user_name = input("🙋Enter the users_name:")
    user_id = input("🙋Enter your user id :")
    

#============================================================================================


# ATM MENU ===================================================================================
def Users_atm_menu():
     while True:
         print("🏧====ATM MENU====🏧")
         print("1.Deposit Money")
         print("2.Withdraw Money")
         print("3.Check Balance")
         print("4.Transcation History")
         print("5.Show current time ")          
         print("6.Exit")

         choice = input("👉Enter Your choice(1-5):")

         if choice == "1":
             deposit_money()


         elif choice == "2":
             withdraw_money(5001)

         elif choice == "3":
             check_balance()

         elif choice =="4":
             add_transaction(TRANSACTION_HISTORY_FILE, 1, 100.50, "Deposit")
             view_transactions(TRANSACTION_HISTORY_FILE)

         elif choice =="5":
            show_current_date()      

         elif choice == "6":
             print("Thank you for using this mini banking system.Good Bye.!😊.")
             exit()
             break
         else:
             print("❌Enter the one to five numbers only!.")



# Login ===========================================================================================

while True:

    print('🙋 Welcome to my mini banking app')
    print('1.Admin Login')
    print('2.Users login')
    print('3.Exit')

    choice = input('👉 Enter your choice(1 to 3):')

    if choice == '1':
        admin_login()
        admin_atm_menu()

    elif choice == '2':
        users_login()
        Users_atm_menu()
        break

    elif choice == '3':
        exit()

    else :
        print('❌Enter the one to three number only!')