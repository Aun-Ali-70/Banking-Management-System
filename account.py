from datetime import date
class Account:
    def __init__(self, account_number, customer, balance, date_opened, status = "Active"):
        self.account_number = account_number
        self.customer = customer
        self.balance = balance
        self.date_opened = date_opened
        self.status = status
    def deposit(self, amount):
        if self.status != "Active":
            print("Account is not active.")
            return False
        if amount<=0:
            print("Deposit amount must be greater than zero.")
            return False
        self.balance += amount
        print(f"Rs. {amount} added successfully.")
        return True
    def withdraw(self, amount):
        if self.status !="Active":
            print("Account is not active.")
            return False
        if amount<=0:
            print("Withdraw amount must be greater than zero.")
            return False
        if amount<=self.balance:
            self.balance -= amount
            print(f"Rs. {amount} withdrawn from your account.")
            print(f"Current Balance: Rs. {self.balance}")
            return True
        else:
            print("Insufficient Balance.")
            return False
    def check_balance(self):
        print(f"You have Rs .{self.balance} in your account.")
    def display_account(self):
        print(f"\n\nAccount Number : {self.account_number}")
        print(f"Account Customer : {self.customer.name}")
        print(f"Opening Date : {self.date_opened}")
        print(f"Account Balance : {self.balance}")
        print(f"Account Status : {self.status}\n\n")
    def to_dict(self):
        return {
            "account_number" : self.account_number,
            "person_id" : self.customer.person_id,
            "balance" : self.balance,
            "date_opened" : self.date_opened.isoformat(),
            "status" : self.status
        }
    @classmethod
    def from_dict(cls, data, customer):
        return cls(
            data["account_number"],
            customer,
            data["balance"],
            date.fromisoformat(data["date_opened"]),
            data["status"]
        )