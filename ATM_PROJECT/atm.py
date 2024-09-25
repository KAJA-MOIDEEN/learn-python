 # Data structure to store user details
users = {
        123: {"name":"kaja","bank_balance": 1000, "account_type": "Savings"},
        456: {"name":"nazeer","bank_balance": 5000, "account_type": "Current"},
        786: {"name":"roshni","bank_balance": 3000, "account_type": "Savings"}
}
class Atm():
    
    def __init__(self,users,bankName):
        print(f'''Wellcome to {bankName} Bank ATM''')
        self.users =  users
        self.bankName = bankName
        
    # Function for Current account transactions
    def current(self,users_data):
        print("Account Holder Name: ",users_data["name"].upper())
        print("Your Account Type: Current")
        transaction = int(input(f'''Please select your transaction :
1.Deposit
2.Withdraw
3.Balance'''))
        
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
            print(f'''Thank you for Visiting {self.bankName} ''')
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
    def savings(self,users_data):
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
    def atm(self):
        while True:
            pin = int(input("Enter Your ATM Pin Number: "))
            
            if pin in self.users:
                print("Pin is correct!")
                users_data = self.users[pin]
                account_type = int(input("Please Select Your Account Type (Enter 1 for Savings or 2 for Current): "))
                
                if account_type == 1:
                    self.savings(users_data)
                elif account_type == 2:
                    self.current(users_data)
                else:
                    print("Invalid Account Type selected!")
            else:
                print("Incorrect Pin Number! Try again.\n")


# Create an ATM object and start the process 

kaja = Atm(users,"kotak")
kaja.atm()

nazeer = Atm(users,"SBI")
kaja.atm()

roshni = Atm(users,"IOB")
roshni.atm()

