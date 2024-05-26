import withdrawal
import Deposit
import bills

current_balance = 5000.00
retry = 0
customersAndPin = {1234: "John Solomon", 2345: "Cynthia David", 3456: "Grace Peter"}

while retry <= 2:
    try:
        pin = int(input("Enter your pin: "))
    except ValueError:
        retry +=1
        if retry == 1:
            print("two more trials, kindly enter a valid input")
        elif retry == 2:
            print("one more trial, kindly enter a valid input")
        else: 
            print("You have been logged out, kindly log in again!")
        continue
    if pin in customersAndPin.keys():
        print("Login successful!")
        print(f"Welcome {customersAndPin.get(pin)}!")
        while True:
            try:
                user_input = int(input("What would you like to do today? \n"""
                                    "Press 1 to Check account balance \n"
                                    "Press 2 to Withdraw \n"
                                    "Press 3 to Deposit \n"
                                    "Press 4 to Pay Utility bill \n"
                                    "Press 5 to Exit \n: "))
            except ValueError:
                print("Error! value must be an integer")
                continue
            if user_input == 1:
                print(f"Account balance is: {current_balance}")
            elif user_input == 2:
                amount = float(input("Enter amount to withdraw: "))
                current_balance = withdrawal.withdraw(current_balance, amount)
            elif user_input == 3:
                amount = float(input("Enter amount to deposit: "))
                current_balance = Deposit.deposit(current_balance, amount)
            elif user_input == 4:
                current_balance = bills.bill(current_balance)
            elif user_input == 5:
                print("Exiting...")
                break
            else:
                print("Invalid option. Please try again.")
            main = input("Do you want to perform another transaction? (yes or no): ").lower()
            if main != "yes":
                print("Thank you for using our services!")
                break
        if main != "yes":
            break
        break
    else:
        retry += 1
        if retry == 1:
            print("Invalid pin, you have two trials left!")
        elif retry == 2:
            print("Invalid pin, you have one trial left!")
        else:
            print("you have been logged out, Kindly login again")
            break
