import Recharge
import dstv_subscription
import gotv_subscription


def bill(account_balance):
    while True:
        option = int(input("Select the utility you want to pay for \n"
                        "1. for Recharge card\n"
                        "2. for dstv subscription\n"
                        "3. for gotv subscription\n"
                        "4. Cancel\n"
                        ": "))
        if option == 1:
            phone_number = input("Enter phone number: ")
            amount = float(input("Enter amount to recharge: "))
            account_balance = Recharge.recharge(phone_number, amount, account_balance)
        elif option == 2:
            dstv_number = input("Enter dstv number: ")
            amount = float(input("Enter amount to pay: "))
            account_balance = dstv_subscription.subscription(dstv_number, amount, account_balance)
        elif option == 3:
            gotv_number = input("Enter gotv number: ")
            amount = float(input("Enter amount to pay: "))
            account_balance = gotv_subscription.subscription(gotv_number, amount, account_balance)
        elif option == 4:
            break
        else:
            print("Invalid option, try again")
            bill(account_balance)
        break
    return account_balance


