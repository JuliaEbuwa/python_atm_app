def deposit(deposit_amount, amount):
    if amount <= 0:
        print("Invalid amount")
    else:
        deposit_amount += amount
        print("Deposit Successful")
        print(f"Current account balance is: {deposit_amount}")
    return deposit_amount
