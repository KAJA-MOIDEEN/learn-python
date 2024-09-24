# Data structure to store user details
users = {
    123: {"name":"kaja","bank_balance": 1000, "account_type": "Savings"},
    456: {"name":"moideen","bank_balance": 5000, "account_type": "Current"},
    786: {"name":"saira","bank_balance": 3000, "account_type": "Savings"}
}
# Function for Current account transactions
def current(users_data ):
    print("Account Holder Name: ",users_data["name"].upper())
    print("Your Account Type: Current")
    transaction = int(input("Please select your transaction type (Enter 1 for Deposit or 2 for Withdraw): "))
    
    if transaction == 1:  # Deposit case
        amount = int(input("Enter Amount to Deposit: "))
        users_data["bank_balance"] += amount
        print("Amount deposited successfully!")
    
    elif transaction == 2:  # Withdraw case
        amount = int(input("Enter Amount to Withdraw: "))
        users_data["bank_balance"] -= amount
        print("Amount withdrawn successfully!")
    elif transaction == 3:
        print(f"Your bank balance: ",users_data["bank_balance"])
        return
    else:
        print("Invalid transaction type!")

    # Check if user wants to check the balance
    check_balance = input("Do you want to check your balance? (Enter 'yes' or 'no'): ").lower()
    if check_balance == "yes":
        print(f"Your bank balance: ",users_data["bank_balance"])
    
    print("Thank you for using our services!\n")
    return users_data["bank_balance"]

# Function for Savings account transactions
def savings(users_data):
    print("Account Holder Name: ",users_data["name"].upper())
    print("Your Account Type: Savings")
    transaction = int(input("Please select your transaction type (Enter 1 for Deposit or 2 for Withdraw 3 for Bank balance): "))
    
    if transaction == 1:  # Deposit case
        amount = int(input("Enter Amount to Deposit: "))
        users_data["bank_balance"] += amount
        print("Amount deposited successfully!")
    
    elif transaction == 2:  # Withdraw case
        amount = int(input("Enter Amount to Withdraw: "))
        users_data["bank_balance"] -= amount
        print("Amount withdrawn successfully!")
    elif  transaction == 3:
        print(f"Your bank balance: ",users_data["bank_balance"])
        return
    else:
        print("Invalid transaction type!")
    
    # Check if user wants to check the balance
    check_balance = input("Do you want to check your balance? (Enter 'yes' or 'no'): ").lower()
    if check_balance == "yes":
        print(f"Your bank balance: ",users_data["bank_balance"])
    
    print("Thank you for using our services!\n")
    return users_data["bank_balance"]

# ATM function to handle user authentication and account type selection
def atm(users):
    while True:
        pin = int(input("Enter Your ATM Pin Number: "))
        
        if pin in users:
            print("Pin is correct!")
            users_data = users[pin]
            account_type = int(input("Please Select Your Account Type (Enter 1 for Savings or 2 for Current): "))
            
            if account_type == 1:
                savings(users_data)
            elif account_type == 2:
                current(users_data)
            else:
                print("Invalid Account Type selected!")
        else:
            print("Incorrect Pin Number! Try again.\n")

# Start the ATM process
atm(users)
