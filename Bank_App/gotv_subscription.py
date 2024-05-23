def subscription(gotv_number, amount, current_balance):
    print(f"{gotv_number} has been recharged with {amount}")
    current_balance -= amount
    print(f"Account balance is {current_balance}")
    return current_balance

