def recharge(phone_number, amount, current_balance):
    print(f"{phone_number} has been recharged with {amount}")
    current_balance -= amount
    print(f"current account balance is {current_balance}")
