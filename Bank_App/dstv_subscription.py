def subscription(dstv_number, amount, current_balance):
    print(f"{dstv_number} has been recharged with {amount}")
    current_balance -= amount
    print(f"current account balance is {current_balance}")
    return current_balance

