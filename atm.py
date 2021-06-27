class ATM:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def checkbalance(self):
        print("Your balance in your account is 5000")

    def withdraw(self, amount):
        newamount = 5000 - amount
        print("You have withdrawn "+str(amount)+" dollars. Your remaining balance is "+str(newamount))

def main():
    print("You have 50,000 dollars in your bank account.")
    usercardnumber = input("Insert your bank card number: ")
    userpin = input("Insert your bank card pin: ")

    user = ATM(usercardnumber, userpin)
    print('Choose what you want to do:')
    print('1. Balance enquiry')
    print('2. Cash withdrawl')
    activity = int(input("Enter activity number: "))

    if (activity == 1):
        user.checkbalance()
    if (activity == 2):
        amount = int(input("Enter the amount to withdraw: "))
        user.withdraw(amount)
    elif (activity!=1 and 2):
        print("Please enter either 1 or 2")
if __name__ == "__main__":
    main()