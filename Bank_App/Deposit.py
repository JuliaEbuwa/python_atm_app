def deposit(account_balance, amount):
    if amount <= 0:
        print("Invalid amount")
    else:
        account_balance += amount
        print("Deposit Successful")
        print(f"Account balance is: {account_balance}")
    return account_balance