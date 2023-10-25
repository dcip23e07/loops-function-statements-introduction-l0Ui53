balance = 2000
min_wd = 50
max_wd = 1000

def ATM(withdrawal: int):
    choice = input("Do you want to withdraw money? Type 'yes' or 'no': ")
    if choice == "no":
        print("goodbye")
        return
    elif choice == 'yes':
        valid_amount = False
        while not valid_amount:
            amount = int(input("How much? "))
            if amount < min_wd:
                amount = int(input("the minimum allowed is 50, please enter again: "))
            elif amount > max_wd:
                amount = int(input("the maximum allowed is 1000. please enter again: "))  
            else:
                print("thank you. please take your money")
                break
ATM(0)  
    

ATM(withdrawal=0)