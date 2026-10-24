from employee import Employee
from datetime import date
class BankManager(Employee):
    def __init__(self, person_id, name, phone, email, post_code, employee_id, salary, date_joined, status = "Active"):
        super().__init__(person_id, name, phone, email, post_code, employee_id, "Bank Manager", salary, date_joined, status)
    def add_employee(self, bank, employee):
        return bank.add_employee(employee)
    def remove_employee(self, bank, employee_id):
        return bank.remove_employee(employee_id)
    def view_all_employees(self, bank):
        return bank.display_employees()
    def view_all_accounts(self, bank):
        bank.display_accounts()
    def view_all_customers(self, bank):
        bank.display_customers()
    def view_bank_report(self, bank):
        report = bank.generate_report()
        for key, value in report.items():
            print(f"{key}: {value}")
    def to_dict(self):
        return super().to_dict()
    @classmethod
    def from_dict(cls, data):
        data = data.copy()
        data.pop("designation", None)
        data["date_joined"] = date.fromisoformat(data["date_joined"])
        
        return cls(**data)