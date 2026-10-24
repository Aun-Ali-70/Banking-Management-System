import json
import os
from saving_account import Saving_Account
from current_account import Current_Account
from account import Account
from customer import Customer
from deposit import Deposit
from withdraw import Withdraw
from transfer import Transfer
from employee import Employee
class File_Manager:
    @staticmethod
    def save_customer(customers, filename):
        customers_data = []
        for customer in customers:
            customer = customer.to_dict()
            customers_data.append(customer)
        with open(filename, "w") as file:
            json.dump(customers_data, file, indent=4)
    @staticmethod
    def load_customers(filename):
        customers = []
        with open(filename, "r") as file:
            customer_data = json.load(file)
        for data in customer_data:
            customer = Customer.from_dict(data)
            customers.append(customer)
        return customers
    @staticmethod
    def save_accounts(accounts, filename):
        accounts_list = []
        for account in accounts:
            data = account.to_dict()
            accounts_list.append(data)
        with open(filename, "w") as file:
            json.dump(accounts_list, file, indent=4)
    @staticmethod
    def load_accounts(filename, bank):
        with open(filename, "r") as file:
            accounts = json.load(file)
        accounts_list = []
        for account in accounts:
            customer_id = account["person_id"]
            customer = bank.search_customer(customer_id)
            if not customer:
                print(f"Customer {customer_id} not found. Account skipped.")
                continue
            account_type = account["account_type"].lower()
            if account_type == "saving":
                acc = Saving_Account.from_dict(account, customer)
            elif account_type == "current":
                acc = Current_Account.from_dict(account, customer)
            else:
                print("Invalid account type.")
                continue

            accounts_list.append(acc)
            customer.accounts.append(acc)

        return accounts_list
    @staticmethod
    def save_transactions(transactions, filename):
        transactions_data = []
        for transaction in transactions:
            transaction = transaction.to_dict()
            transactions_data.append(transaction)
        with open(filename, "w") as file:
            json.dump(transactions_data, file, indent=4)
    @staticmethod
    def load_transactions(filename, bank):
        with open(filename, "r") as file:
            transactions = json.load(file)
        transactions_list = []
        for transaction in transactions:
            account = bank.search_account(transaction["account_number"])
            if account is None:
                print(
                    f"Account {transaction['account_number']} "
                    "not found. Transaction skipped."
                )
                continue
            transaction_type = transaction["transaction_type"]
            transaction_type = transaction_type.lower()
            if transaction_type == "deposit":
                trans = Deposit.from_dict(transaction, account)
            elif transaction_type == "withdraw":
                trans =  Withdraw.from_dict(transaction, account)
            elif transaction_type == "transfer":
                source_destination = bank.search_account(transaction["destination_account_number"])
                if source_destination is None:
                    print(
                        f"Destination account "
                        f"{transaction['destination_account_number']} "
                        "not found. Transaction skipped."
                    )
                    continue
                trans = Transfer.from_dict(transaction, account, source_destination)
            else:
                print("Invalid transaction type. Transaction skipped.")
                continue
            transactions_list.append(trans)
        return transactions_list
    @staticmethod
    def append_record(record, filename):
        data = record.to_dict()
        with open(filename, "r") as file:
            records = json.load(file)
        records.append(data)
        with open(filename, "w") as file:
            json.dump(records, file, indent=4)
    @staticmethod
    def delete_file(filename):
        if os.path.exists(filename):
            os.remove(filename)
            return True
        print("File Doesn't exist.")
        return False
    @staticmethod
    def clear_file(filename):
        if os.path.exists(filename):
            with open(filename, "w") as file:
                json.dump([], file, indent=4)
                return True
        print("File doesn't exist.")
        return False
    @staticmethod
    def save_employees(employees, filename):
        employees_dict = []
        for employee in employees:
            employee_dict = employee.to_dict()
            employees_dict.append(employee_dict)
        with open(filename, "w") as file:
            json.dump(employees_dict, file, indent = 4)
    @staticmethod
    def load_employees(filename):
        with open(filename, "r") as file:
            employees_dict = json.load(file)
        employees_list = []
        for employee_dict in employees_dict:
            employee = Employee.from_dict(employee_dict)
            employees_list.append(employee)
        return employees_list