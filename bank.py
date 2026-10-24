from datetime import date
from saving_account import Saving_Account
from current_account import Current_Account
class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.accounts = []
        self.employees = []
        self.transactions = []
    def generate_employee_id(self):
        if not self.employees:
            return 108367320
        highest_employee_id = max(
            employee.employee_id for employee in self.employees
        )
        return highest_employee_id + 13
    def generate_customer_id(self):
        if not self.customers:
            return 100042345
        highest_customer_id = max(
            customer.person_id for customer in self.customers
        )
        return highest_customer_id+3
    def generate_transaction_id(self):
        if not self.transactions:
            return 128030439
        highest_transaction_id = max(
            transaction.transaction_id for transaction in self.transactions
        )
        return highest_transaction_id+9
    @staticmethod
    def date_today():
        return date.today()
    def generate_account_number(self):
        if not self.accounts:
            return 100001
        highest_account_number = max(
            account.account_number for account in self.accounts
        )
        return highest_account_number+1
    def create_account(self, customer, account_type, initial_balance):
        account_type = account_type.strip().lower()
        account_number = self.generate_account_number()
        date_opened = date.today()
        
        if account_type == "saving":
            interest_rate = 5.0
            saving_account = Saving_Account(account_number, customer, initial_balance, date_opened, interest_rate)
            if self.add_account(saving_account):
                return saving_account
            return False
        elif account_type == "current":
            overdraft_limit = 5000
            current_account = Current_Account(account_number, customer, initial_balance, date_opened, overdraft_limit)
            if self.add_account(current_account):
                return current_account
            return False
        else:
            print("Invalid Input.")
            return False
    def add_customer(self, customer):
        for i in self.customers:
            if i.person_id == customer.person_id:
                print(f"Customer with {customer.person_id} already exists.")
                return False
        self.customers.append(customer)
        print(f"Customer with {customer.person_id} added successfully.")
        return True
    def remove_customer(self, customer):
        for i in self.customers:
            if i.person_id == customer.person_id:
                if i.accounts:
                    print("Customer cannot be deleted because they still have accounts.")
                    return False
                else:
                    self.customers.remove(i)
                    print(f"Customer with {customer.person_id} deleted successfully.")
                    return True
        else:
            print(f"Customer with {customer.person_id} doesn't exist.")
            return False
    def search_customer(self, person_id):
        for customer in self.customers:
            if customer.person_id == person_id:
                return customer
        return None
    def display_customers(self):
        if not self.customers:
            print("No customer found.")
            return
        for customer in self.customers:
            customer.display_customer()
    def add_account(self, account):
        for i in self.accounts:
            if i.account_number == account.account_number:
                print(f"Account with number {account.account_number} already exists.")
                return False
        customer = self.search_customer(account.customer.person_id)
        if customer is None:
            print("Customer isn't registered with bank")
            return False
        if customer.status != "Active":
            print("Customer is not active.")
            return False
        self.accounts.append(account)
        customer.accounts.append(account)
        print(f"Account {account.account_number} added successfully.")
        return True
    def remove_account(self, account_number):
        account = self.search_account(account_number)
        if account is None:
            return False
        self.accounts.remove(account)
        account.customer.accounts.remove(account)
        print("Account Deleted Successfully.")
        return True
    def search_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None
    def display_accounts(self):
        if not self.accounts:
            print("No accounts found.")
            return
        for account in self.accounts:
            account.display_account()
    def add_employee(self, employee):
        for emp in self.employees:
            if emp.employee_id == employee.employee_id:
                print(f"Employee with ID {employee.employee_id} already exists.")
                return False
            if employee.designation == "Bank Manager":
                for emp in self.employees:
                    if emp.designation == "Bank Manager":
                        print("Bank manager already exists.")
                        return False
        self.employees.append(employee)
        print(f"Employee with ID {employee.employee_id} added successfully.")
        return True
    def remove_employee(self, employee_id):
        for emp in self.employees:
            if emp.employee_id == employee_id:
                self.employees.remove(emp)
                print(f"Employee with ID {employee_id} deleted successfully.")
                return True
        print(f"Employee with ID {employee_id} not found.")
        return False
    def search_employee(self, employee_id):
        for emp in self.employees:
            if emp.employee_id == employee_id:
                return emp
        return None
    def display_employees(self):
        if not self.employees:
            print("No employee found")
            return
        for emp in self.employees:
            emp.display()
    def count_saving_accounts(self):
        saving = 0
        for account in self.accounts:
            if isinstance(account, Saving_Account):
                saving += 1
        return saving
    def count_current_accounts(self):
        current = 0
        for account in self.accounts:
            if isinstance(account, Current_Account):
                current += 1
        return current
    def count_active_accounts(self):
        active = 0
        for account in self.accounts:
            if account.status == "Active":
                active += 1
        return active
    def total_bank_balance(self):
        balance = 0
        for account in self.accounts:
            balance += account.balance
        return balance
    def search_transaction(self, transaction_id):
        for transaction in self.transactions:
            if transaction.transaction_id == transaction_id:
                return transaction
        print(f"Transaction with {transaction_id} not found.")
        return None
    def display_transactions_by_account(self, account_number):
        found = False
        for transaction in self.transactions:
            if transaction.account.account_number == account_number:
                transaction.display_transaction()
                found = True
        if not found:
            print(f"No transactions found for {account_number}.")
    def display_transactions_by_type(self, transaction_type):
        found = False
        for transaction in self.transactions:
            if transaction.transaction_type.lower() == transaction_type.lower():
                transaction.display_transaction()
                found = True
        if not found:
            print(f"No transactions found.")
    def generate_report(self):
        report = {}
        report["Bank Name"] = self.name
        report["Total Customers"] = len(self.customers)
        report["Total Employees"] = len(self.employees)
        report["Total Accounts"] = len(self.accounts)
        report["Total Saving Accounts"] = self.count_saving_accounts()
        report["Total Current Accounts"] = self.count_current_accounts()
        report["Total Active Accounts"] = self.count_active_accounts()
        report["Total Inactive Accounts"] = len(self.accounts) - self.count_active_accounts()
        report["Total Bank Balance"] = self.total_bank_balance()
        report["Total Transactions"] = len(self.transactions)
        return report