import Recharge
import dstv_subscription
import gotv_subscription


def bill(current_balance):
    while True:
        option = int(input("Select the utility you want to pay for \n"
                        "1. for Recharge card\n"
                        "2. for dstv subscription\n"
                        "3. for gotv subscription\n"
                        "4. Cancel\n"
                        ": "))
        # if 3 >= option > 0:
        if option == 1:
            phone_number = input("Enter phone number: ")
            amount = float(input("Enter amount to recharge: "))
            current_balance = Recharge.recharge(phone_number, amount, current_balance)
        elif option == 2:
            dstv_number = input("Enter dstv number: ")
            amount = float(input("Enter amount to pay: "))
            current_balance = dstv_subscription.subscription(dstv_number, amount, current_balance)
        elif option == 3:
            gotv_number = input("Enter gotv number: ")
            amount = float(input("Enter amount to pay: "))
            current_balance = gotv_subscription.subscription(gotv_number, amount, current_balance)
        elif option == 4:
            break
        else:
            print("Invalid option, try again")
            bill(current_balance)
        break
    return current_balance


