from transaction import Transaction
from validator import Validator
from datetime import date
class Withdraw(Transaction):
    def __init__(self, transaction_id, account, amount, transaction_date, status="Success"):
        super().__init__(transaction_id, account, amount, transaction_date, "Withdraw", status)
    def execute(self):
        if not Validator.validate_amount(self.amount):
            self.status = "Failed"
            return False
        if self.account.withdraw(self.amount):
            self.status = "Success"
            return True
        else:
            self.status = "Failed"
            return False
    @classmethod
    def from_dict(cls, data, account):
        return cls(
            data["transaction_id"],
            account,
            data["amount"],
            date.fromisoformat(data["transaction_date"]),
            data["status"]
        )