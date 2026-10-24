from account import Account
from datetime import date
class Current_Account(Account):
    def __init__(self, account_number, customer, balance, date_opened, overdraft_limit, status = "Active"):
        super().__init__(account_number, customer, balance, date_opened, status)
        self.overdraft_limit = overdraft_limit
    def set_overdraft_limit(self, new_overdraft_limit):
        if new_overdraft_limit<0:
            print("Overdraft limit cannot be negative.")
            return False
        self.overdraft_limit = new_overdraft_limit
        return True
    def check_overdraft(self, amount_requested):
        if amount_requested>0:
            max_withdrawal = self.balance+self.overdraft_limit
            if amount_requested<=max_withdrawal:
                return True
            return False
        return False
    def withdraw(self, amount):
        if self.status!= "Active":
            print("Account is not active.")
            return False
        if amount<=0:
            print("Withdrawal amount must be greater than zero.")
            return False
        if not self.check_overdraft(amount):
            print("Overdraft limit exceed.")
            return False
        self.balance -= amount
        print(f"Rs .{amount} withdrew from your account.")
        print(f"Current Balance Rs .{self.balance}")
        return True
    def to_dict(self):
        data = super().to_dict()
        data["account_type"] = "Current"
        data["overdraft_limit"] = self.overdraft_limit
        return data
    @classmethod
    def from_dict(cls, data, customer):
        return cls(
            data["account_number"],
            customer,
            data["balance"],
            date.fromisoformat(data["date_opened"]),
            data["overdraft_limit"],
            data["status"]
        )