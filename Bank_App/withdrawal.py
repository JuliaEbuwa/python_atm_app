def withdraw(initial_balance, amount):
    if amount < 0:
        print("Invalid amount, amount must be greater than 0")
    elif amount > initial_balance:
        print("Insufficient funds!")
    else:
        print("withdrawal successful!")
        initial_balance -= amount
        print(f"current balance is: {initial_balance} ")
    return initial_balance

