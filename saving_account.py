from account import Account
from datetime import date
class Saving_Account(Account):
    def __init__(self, account_number, customer, balance, date_opened, interest_rate, status="Active"):
        super().__init__(account_number, customer, balance, date_opened, status)
        self.interest_rate = interest_rate
    def calculate_interest(self):
        if self.status!="Active":
            print("Account is not active.")
            return
        interest = self.balance * self.interest_rate/100
        return interest
    def to_dict(self):
        data = super().to_dict()
        data["account_type"] = "Saving"
        data["interest_rate"] = self.interest_rate
        return data
    @classmethod
    def from_dict(cls, data, customer):
        return cls(
            data["account_number"],
            customer,
            data["balance"],
            date.fromisoformat(data["date_opened"]),
            data["interest_rate"],
            data["status"]
        )