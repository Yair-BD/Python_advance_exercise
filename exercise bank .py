def bank():
    class BankAccount:
        bank_name = "YourPay"

        def __init__(self, balance=0):
            self.name = "User name"
            self.balance = balance

        def greet(self, name):
            print(f"Welcome {name} :) \nwhat would you like todo ?  ")

        def deposit(self, money):
            self.balance += money
            print("Your request has been made")
            self.print_balance()

        def withdraw(self, money):
            self.balance -= money
            print("Your request has been made")
            self.print_balance()

        def print_balance(self):
            print(f"Your balance is standing on {self.balance} NIS")

    def main():
        name = input("Enter a name:")
        yair_account = BankAccount()
        yair_account.greet("Yair")
        nurit_account = BankAccount()
        nurit_account.greet("Nurit")
        yair_account.deposit(100)
        yair_account.deposit(300)
        transferred_account = BankAccount(500)


    main()


if __name__ == '__main__':
    bank()


