atm_pin = 123
bank_balance = 1000
a = True
while a:
    pin = input("Enter the pin_number: ")
    if atm_pin == int(pin):
        print("pin is correct")
        account = input("Enter Account Type Savings or Current: ")
        if account.lower() == "savings":
            print("Account Type: ",account)
            trastation = input("Enter Your Transaction Type (Deposit/Withdrow):")
            if trastation.lower() == "deposit":
                amount = int(input("Enter Amount: "))
                bank_balance  += amount
                print("Amount deposit Successfully")
                check_balance  = input("Do you want to check balance? (yes/no): ")
                if  check_balance.lower() == "yes":
                    print("bank balance:",bank_balance)
                    print("Thank You ...! ")
                    break
                else:
                    print("Thank You ...! ")
                    break
            else:
                amount = int(input("Enter Amount: "))
                bank_balance  -= amount
                print("Amount withdraw Successfully")
                check_balance  = input("Do you want to check balance? (yes/no): ")
                if  check_balance.lower() == "yes":
                    print("bank balance:",bank_balance)
                    print("Thank You ...! ")
                    break
                else:
                    print("Thank You ...! ")
                    break
        elif account.lower() == "current":
            print("Account Type: ",account)
            trastation = input("Enter Your Transaction Type (Deposit/Withdrow):")
            if trastation.lower() == "deposit":
                amount = int(input("Enter Amount: "))
                bank_balance  += amount
                print("Amount deposit Successfully")
                check_balance  = input("Do you want to check balance? (yes/no): ")
                if  check_balance.lower() == "yes":
                    print("bank balance:",bank_balance)
                    print("Thank You ...! ")
                    break
                else:
                    print("Thank You ...! ")
                    break
            else:
                amount = int(input("Enter Amount: "))
                bank_balance  -= amount
                print("Amount withdrow Successfully")
                check_balance  = input("Do you want to check balance? (yes/no): ")
                if  check_balance.lower() == "yes":
                    print("bank balance:",bank_balance)
                    break
                else:
                    print("Thank You ...! ")
                    break
        else:   
            print("Incorrect Account Type")    
    else:
        print("Pin Number Incorrect")