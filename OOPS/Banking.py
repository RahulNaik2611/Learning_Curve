class Atm:

    # Constructor
    def __init__(self):
        self.pin = ' '
        self.balance = 0
        self.menu()


    def menu(self):
        user_input = input("""
        Hi how can I help you?
        1. press 1 to create pin
        2. press 2 to change pin
        3. press 3 to check balance
        4. press 4 to withdraw
        5. press 5 to deposit
        6. Anything else to exit
        """)

        if user_input == '1':
            self.create_pin()

            #create pin
        elif user_input =='2':
            self.change_pin()
            # Change pin
        elif user_input=='3':
            self.check_balance()
            #check balance
        elif user_input == '4':
            self.withdraw()
            #withdraw amount
        elif user_input == '5':
            self.deposit()

            #Deposit the amount into bank
        else:
            print("Please enter a valid input")
            exit()

    def create_pin(self):
        user_pin = input("Enter your pin : ")
        self.pin = user_pin

        user_balance = int(input("Enter your balance : "))
        self.balance = user_balance

        print(f'your pin created: {self.pin}')
        self.menu()

    def change_pin(self):

        previous_pin = input("Enter your previous pin : ")

        if previous_pin == self.pin:
            new_pin = input("Enter your new pin : ")
            self.pin = new_pin
            print(f'Your change successfully: {self.pin}')
            self.menu()
            #let him change the pin
        else:
            print("Your not able to change your pin !")
            self.menu()

    def check_balance(self):
        user_pin = input("Enter your pin : ")
        if user_pin == self.pin:
            print("Your balance is: ", self.balance)
            self.menu()
        else:
            print("Your not able to change your pin !")
            self.menu()


    def withdraw(self):
        user_pin = input("Enter your pin : ")
        if user_pin == self.pin:
            withdraw_amount = int(input("Enter your withdraw amount : "))
            if withdraw_amount <= self.balance:
                self.balance -= withdraw_amount
                print(f'Your withdraw successfully: {self.balance}')
                self.menu()
            else:
                print("you dont have enough money to withdraw")
        else:
            print("Enter the pin correctly ")
            self.menu()

    def deposit(self):
        user_pin = input("Enter your pin : ")
        if user_pin == self.pin:
            deposit_amount = int(input("Enter your deposit amount : "))
            self.balance += deposit_amount
            print(f'Your deposit successfully: {self.balance}')
            self.menu()
        else:
            print("Enter the pin correctly ")



obj = Atm()