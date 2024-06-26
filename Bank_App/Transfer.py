def transfer(account_balance, amount):
    account_details = input("Enter account number to transfer to: ")
    bank_name = input("Enter destination bank: ")
    if amount <= 0:
        print("Invalid amount, amount must be greater than 0")
    elif amount > account_balance:
        print("Insufficient funds!")
    else:
        print(f"transfer to {account_details} of {bank_name} was successful!")
        account_balance -= amount
        print(f"account balance is: {account_balance} ")
    return account_balance