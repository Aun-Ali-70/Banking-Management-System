from transaction import Transaction
from datetime import date
from validator import Validator
class Transfer(Transaction):
    def __init__(self, transaction_id, account, amount, transaction_date, destination_account, status="Pending"):
        super().__init__(transaction_id, account, amount, transaction_date, "Transfer", status)
        self.destination_account = destination_account
    def execute(self):
        if self.account.account_number == self.destination_account.account_number:
            print("Both Source account and destination account are same.")
            self.status = "Failed"
            return False
        if not Validator.validate_amount(self.amount):
            self.status = "Failed"
            return False
        if not self.account.withdraw(self.amount):
            self.status = "Failed"
            return False
        if not self.destination_account.deposit(self.amount):
            self.account.deposit(self.amount)
            self.status = "Failed"
            return False
        self.status = "Success"
        return True
    def display_transaction(self):
        super().display_transaction()
        print(f"Destination Account: {self.destination_account.account_number}")
    def to_dict(self):
        return {
            "transaction_id" : self.transaction_id,
            "account_number" : self.account.account_number,
            "amount" : self.amount,
            "transaction_date" : self.transaction_date.isoformat(),
            "destination_account_number" : self.destination_account.account_number,
            "transaction_type" : self.transaction_type,
            "status" : self.status
        }
    @classmethod
    def from_dict(cls, data, account, destination_account):
        return cls(
            data["transaction_id"],
            account,
            data["amount"],
            date.fromisoformat(data["transaction_date"]),
            destination_account,
            data["status"]
        )