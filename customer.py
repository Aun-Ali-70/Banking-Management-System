from person import Person
from datetime import date
class Customer(Person):
    def __init__(self, person_id, name, phone, email, post_code, date_joined, status = "Active"):
        super().__init__(person_id, name, phone, email, post_code)
        self.date_joined = date_joined
        self.status = status
        self.accounts = []
    def display_customer(self):
        self.display_info()
        print(f"Date joined : {self.date_joined}")
        print(f"Status : {self.status}")
    def open_account(self, bank, account_type, initial_balance):
        return bank.create_account(self, account_type, initial_balance)
    def close_account(self, bank, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return bank.remove_account(account_number)
        print("This account does not belong to this customer.")
        return False
    def view_accounts(self):
        if not self.accounts:
            print("No account found.")
            return
        for account in self.accounts:
            account.display_account()
    def search_account(self, account_number):
        if not self.accounts:
            print("No account found.")
            return None
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None
    def update_customer(self, name=None, phone=None, email=None):
        if name is not None:
            self.update_name(name)
            print("Name updated.")
        if phone is not None:
            self.update_phone(phone)
            print("Phone Updated.")
        if email is not None:
            self.update_email(email)
            print("Email Updated.")
        print("Customer Updated successfully.")
        return True
    def to_dict(self):
        return {
            "person_id": self.person_id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "post_code": self.post_code,
            "date_joined": self.date_joined.isoformat(),
            "status": self.status,
        }
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["person_id"],
            data["name"],
            data["phone"],
            data["email"],
            data["post_code"],
            date.fromisoformat(data["date_joined"]),
            data["status"]
        )