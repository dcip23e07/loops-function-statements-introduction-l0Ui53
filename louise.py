balance:int = 2000
min_wd:int = 50
max_wd:int = 1000

def atm(withdrawal: int):
    choice = input("Do you want to withdraw money? Type 'yes' or 'no': ")
    choice_0 = "no"
    choice_1 = "yes"
    if choice == choice_0:
        print("Goodbye")
    elif choice == choice_1:
        amount = int(input("Please enter amount: "))
        if amount < min_wd:
            amount = int(input("Please enter minimum amount of 50: "))
        elif amount > max_wd:
            amount = int(input("Please enter maximum amount of 1000: "))
        elif amount > balance:
            amount = int(input("This amount exceeds your balance. Please enter again: ")) 
        else:
            print("Thank you. Please take your money!")
    else:
        print(input("Please enter 'yes' or 'no': "))
atm(0)  
