from datetime import date
class Transaction:
    def __init__(self, transaction_id, account, amount, transaction_date, transaction_type, status="Success"):
        self.transaction_id = transaction_id
        self.account = account
        self.amount = amount
        self.transaction_date = transaction_date
        self.transaction_type = transaction_type
        self.status = status
    def execute(self):
        raise NotImplementedError("Subclasses must implement execute().")
    def display_transaction(self):
        print(f"\n\nTransaction ID : {self.transaction_id}")
        print(f"Account Number : {self.account.account_number}")
        print(f"Amount : {self.amount}")
        print(f"Transaction Date : {self.transaction_date}")
        print(f"Transaction Type : {self.transaction_type}")
        print(f"Transaction Status : {self.status}")
    def to_dict(self):
        return {
        "transaction_id": self.transaction_id,
        "account_number": self.account.account_number,
        "amount": self.amount,
        "transaction_date": self.transaction_date.isoformat(),
        "transaction_type": self.transaction_type,
        "status": self.status
    }
    @classmethod
    def from_dict(cls, data, bank):
        account = bank.search_account(data["account_number"])
        return cls(
            transaction_id = data["transaction_id"],
            account = account,
            amount = data["amount"],
            transaction_date = date.fromisoformat(data["transaction_date"]),
            transaction_type = data["transaction_type"],
            status = data["status"]
        )