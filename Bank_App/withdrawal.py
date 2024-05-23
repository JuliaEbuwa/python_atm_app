def withdraw(account_balance, amount):
    if amount <= 0:
        print("Invalid amount, amount must be greater than 0")
    elif amount > account_balance:
        print("Insufficient funds!")
    else:
        print("withdrawal successful!")
        account_balance -= amount
        print(f"account balance is: {account_balance} ")
    return account_balance

