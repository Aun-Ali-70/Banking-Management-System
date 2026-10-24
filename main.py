from bank import Bank
from file_manager import File_Manager
from validator import Validator
from customer import Customer
from deposit import Deposit
from withdraw import Withdraw
from transfer import Transfer
from datetime import date
from employee import Employee


def main():
    bank = Bank("HBL")
    
    customers = File_Manager.load_customers("customers.json")
    bank.customers = customers
    
    accounts = File_Manager.load_accounts("accounts.json", bank)
    bank.accounts = accounts
    
    transactions = File_Manager.load_transactions("transactions.json", bank)
    bank.transactions = transactions
    
    employees = File_Manager.load_employees("employees.json")
    bank.employees = employees
    
    bank_manager = None
    for employee in bank.employees:
        if employee.designation == "Bank Manager":
            bank_manager = employee
            break

    while True:
        print("\n========== BANKING SYSTEM ==========")
        print("1. Customer Management")
        print("2. Account Management")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer")
        print("6. Transaction Management")
        print("7. Bank Report")
        print("8. Save Data")
        print("9. Employee Management")
        print("10. Bank Manager")
        print("11. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("========== CUSTOMER OPERATIONS ==========")
            print("1. Open Account")
            print("2. Close Account")
            print("3. Display Customer")
            print("4. Update Customer")
            print("5. View Customer Accounts")
            print("6. Search Customer Account")
            print("7. Add Customer")
            print("8. Delete Customer")
            print("9. Back to main menu")

            Customer_Operation_Choice = input("Enter your choice: ")

            if Customer_Operation_Choice == "1":
                customer_id = input("Enter the customer ID: ")
                customer = bank.search_customer(int(customer_id))

                if customer:
                    acc_type = input(
                        "Enter account type (Saving/Current): "
                    ).strip().lower()

                    if acc_type not in ["saving", "current"]:
                        print("Invalid account type.")
                        continue

                    initial_balance = input("Enter the initial deposit: ")
                    initial_balance = int(initial_balance)

                    if not Validator.validate_amount(initial_balance):
                        print("Invalid initial deposit.")
                        continue

                    customer.open_account(bank, acc_type, initial_balance)

                else:
                    print("Customer doesn't exist in this bank.")

            elif Customer_Operation_Choice == "2":
                customer_id = input("Enter the customer ID: ")
                customer = bank.search_customer(int(customer_id))

                if customer:
                    account_number = input("Enter account Number: ")
                    account_number = int(account_number)

                    if not Validator.validate_account_number(account_number):
                        print("Invalid account number.")
                        continue

                    customer.close_account(bank, account_number)

                else:
                    print("Customer doesn't exist in this bank.")

            elif Customer_Operation_Choice == "3":
                customer_id = input("Enter the customer ID: ")
                customer = bank.search_customer(int(customer_id))

                if customer:
                    customer.display_customer()
                else:
                    print("Customer doesn't exist in this bank.")

            elif Customer_Operation_Choice == "4":
                customer_id = input("Enter the customer ID: ")
                customer = bank.search_customer(int(customer_id))

                if customer:
                    print("========== UPDATE CUSTOMER ==========")
                    print("What do you want to update?")
                    print("1. Update Name")
                    print("2. Update Phone")
                    print("3. Update Email")
                    print("4. Update Name and Phone")
                    print("5. Update Name and Email")
                    print("6. Update Phone and Email")
                    print("7. Update All")
                    print("8. Back")

                    update_choice = input("Enter your choice: ")

                    if update_choice == "1":
                        new_name = input("Enter Customer's Name to be updated.")
                        if not Validator.validate_name(new_name):
                            print("Invalid name.")
                            continue
                        customer.update_customer(name=new_name)

                    elif update_choice == "2":
                        new_phone = input("Enter Customer's Phone to be updated.")
                        if not Validator.validate_phone(new_phone):
                            print("Invalid phone.")
                            continue
                        customer.update_customer(phone=new_phone)

                    elif update_choice == "3":
                        new_email = input("Enter Customer's Email to be updated.")
                        if not Validator.validate_email(new_email):
                            print("Invalid Email.")
                            continue
                        customer.update_customer(email=new_email)

                    elif update_choice == "4":
                        new_name = input("Enter Customer's Name to be updated.")
                        if not Validator.validate_name(new_name):
                            print("Invalid name.")
                            continue

                        new_phone = input("Enter Customer's Phone to be updated.")
                        if not Validator.validate_phone(new_phone):
                            print("Invalid phone.")
                            continue

                        customer.update_customer(
                            phone=new_phone,
                            name=new_name
                        )

                    elif update_choice == "5":
                        new_name = input("Enter Customer's Name to be updated.")
                        if not Validator.validate_name(new_name):
                            print("Invalid name.")
                            continue

                        new_email = input("Enter Customer's Email to be updated.")
                        if not Validator.validate_email(new_email):
                            print("Invalid Email.")
                            continue

                        customer.update_customer(
                            name=new_name,
                            email=new_email
                        )

                    elif update_choice == "6":
                        new_phone = input("Enter Customer's Phone to be updated.")
                        if not Validator.validate_phone(new_phone):
                            print("Invalid phone.")
                            continue

                        new_email = input("Enter Customer's Email to be updated.")
                        if not Validator.validate_email(new_email):
                            print("Invalid Email.")
                            continue

                        customer.update_customer(
                            phone=new_phone,
                            email=new_email
                        )

                    elif update_choice == "7":
                        new_name = input("Enter Customer's Name to be updated.")
                        if not Validator.validate_name(new_name):
                            print("Invalid name.")
                            continue

                        new_email = input("Enter Customer's Email to be updated.")
                        if not Validator.validate_email(new_email):
                            print("Invalid Email.")
                            continue

                        new_phone = input("Enter Customer's Phone to be updated.")
                        if not Validator.validate_phone(new_phone):
                            print("Invalid phone.")
                            continue

                        customer.update_customer(
                            new_name,
                            new_phone,
                            new_email
                        )

                    elif update_choice == "8":
                        pass

            elif Customer_Operation_Choice == "5":
                customer_id = input("Enter customer ID: ")
                customer = bank.search_customer(int(customer_id))

                if customer:
                    customer.view_accounts()
                else:
                    print("Customer doesn't exist in this bank.")

            elif Customer_Operation_Choice == "6":
                customer_id = input("Enter customer ID: ")
                customer = bank.search_customer(int(customer_id))

                if customer:
                    account_number = input("Enter account number: ")
                    account_number = int(account_number)

                    if not Validator.validate_account_number(account_number):
                        print("Invalid account number.")
                        continue

                    account = customer.search_account(account_number)

                    if account:
                        account.display_account()
                    else:
                        print("Account not found.")

                else:
                    print("Customer doesn't exist in this bank.")

            elif Customer_Operation_Choice == "7":
                name = input("Enter your name: ")

                if not Validator.validate_name(name):
                    print("Invalid name.")
                    continue

                phone = input("Enter your phone: ")

                if not Validator.validate_phone(phone):
                    print("Invalid phone.")
                    continue

                email = input("Enter your email: ")

                if not Validator.validate_email(email):
                    print("Invalid email.")
                    continue

                postcode = input("Enter your postcode: ")

                date_joined = date.today()
                person_id = bank.generate_customer_id()

                customer = Customer(
                    person_id,
                    name,
                    phone,
                    email,
                    postcode,
                    date_joined
                )

                bank.add_customer(customer)

            elif Customer_Operation_Choice == "8":
                customer_id = input("Enter Customer ID: ")
                customer = bank.search_customer(int(customer_id))

                if customer:
                    bank.remove_customer(customer)
                else:
                    print("Customer doesn't exist in this bank.")

            elif Customer_Operation_Choice == "9":
                pass

            else:
                pass

        if choice == "2":
            print("========== ACCOUNT MANAGEMENT ==========")
            print("1. Check Balance")
            print("2. Display Account")
            print("3. Back to Main Menu")

            Account_Management_Choice = input("Enter your choice: ")

            if Account_Management_Choice == "1":
                account_number = input("Enter your Account Number: ")
                account_number = int(account_number)

                if not Validator.validate_account_number(account_number):
                    print("Invalid account number.")
                    continue

                account = bank.search_account(account_number)

                if account:
                    account.check_balance()

            elif Account_Management_Choice == "2":
                account_number = input("Enter your Account Number: ")
                account_number = int(account_number)

                if not Validator.validate_account_number(account_number):
                    print("Invalid account number.")
                    continue

                account = bank.search_account(account_number)

                if account:
                    account.display_account()

            elif Account_Management_Choice == "3":
                pass

        if choice == "3":
            print("========== DEPOSIT ==========")

            account_number = input("Enter your account Number: ")
            account_number = int(account_number)

            if not Validator.validate_account_number(account_number):
                print("Invalid account number.")
                continue

            account = bank.search_account(account_number)

            if account:
                deposit_amount = input("Enter Deposit Amount: ")
                deposit_amount = int(deposit_amount)

                if not Validator.validate_amount(deposit_amount):
                    print("Invalid amount.")
                    continue

                transaction_id = bank.generate_transaction_id()
                transaction_date = bank.date_today()

                deposit = Deposit(
                    transaction_id,
                    account,
                    deposit_amount,
                    transaction_date
                )

                if deposit.execute():
                    bank.transactions.append(deposit)

        if choice == "4":
            print("========== WITHDRAW ==========")

            account_number = input("Enter your account Number: ")
            account_number = int(account_number)

            if not Validator.validate_account_number(account_number):
                print("Invalid account number.")
                continue

            account = bank.search_account(account_number)

            if account:
                withdraw_amount = input("Enter Withdraw Amount: ")
                withdraw_amount = int(withdraw_amount)

                if not Validator.validate_amount(withdraw_amount):
                    print("Invalid amount.")
                    continue

                transaction_id = bank.generate_transaction_id()
                transaction_date = bank.date_today()

                withdraw = Withdraw(
                    transaction_id,
                    account,
                    withdraw_amount,
                    transaction_date
                )

                if withdraw.execute():
                    bank.transactions.append(withdraw)

        if choice == "5":
            print("========== Transfer ==========")

            source_account_number = input(
                "Enter the source account Number: "
            )
            source_account_number = int(source_account_number)

            if not Validator.validate_account_number(source_account_number):
                print("Invalid account number.")
                continue

            source_account = bank.search_account(source_account_number)

            destination_account_number = input(
                "Enter the destination account Number: "
            )
            destination_account_number = int(destination_account_number)

            if not Validator.validate_account_number(destination_account_number):
                print("Invalid account number.")
                continue

            destination_account = bank.search_account(
                destination_account_number
            )

            if source_account and destination_account:
                amount = input("Enter Transfer Amount: ")
                amount = int(amount)

                if not Validator.validate_amount(amount):
                    print("Invalid amount.")
                    continue

                transaction_id = bank.generate_transaction_id()
                transaction_date = bank.date_today()

                transfer = Transfer(
                    transaction_id,
                    source_account,
                    amount,
                    transaction_date,
                    destination_account
                )

                if transfer.execute():
                    bank.transactions.append(transfer)

        if choice == "6":
            print("========== TRANSACTION MANAGEMENT ==========")
            print("1. Display All Transactions")
            print("2. Search Transaction")
            print("3. View Transactions by Account")
            print("4. View Transactions by Type")
            print("5. Back to Main Menu")

            transaction_choice = input("Enter your choice: ")

            if transaction_choice == "1":
                for transaction in bank.transactions:
                    transaction.display_transaction()

            elif transaction_choice == "2":
                transaction_id = input("Enter transaction id: ")
                transaction_id = int(transaction_id)

                transaction = bank.search_transaction(transaction_id)

                if transaction:
                    transaction.display_transaction()

            elif transaction_choice == "3":
                account_number = input("Enter account number: ")
                account_number = int(account_number)

                if not Validator.validate_account_number(account_number):
                    print("Invalid account number.")
                    continue

                bank.display_transactions_by_account(account_number)

            elif transaction_choice == "4":
                transaction_type = input("Enter transaction type: ")
                bank.display_transactions_by_type(transaction_type)

            else:
                pass

        if choice == "7":
            print("========== BANK REPORT ==========")

            report = bank.generate_report()

            for key, value in report.items():
                print(f"{key}: {value}")

        if choice == "8":
            print("========== SAVE DATA ==========")

            File_Manager.save_customer(
                bank.customers,
                "customers.json"
            )

            File_Manager.save_accounts(
                bank.accounts,
                "accounts.json"
            )

            File_Manager.save_transactions(
                bank.transactions,
                "transactions.json"
            )

            File_Manager.save_employees(
                bank.employees,
                "employees.json"
            )

            print("Data saved successfully.")

        if choice == "9":
            print("========== Employee MANAGEMENT ==========")
            print("1. Add Employee")
            print("2. Update Designation")
            print("3. Update Salary")
            print("4. Update Status")
            print("5. Display Employee")
            print("6. View All Employees")
            print("7. Delete Employee")
            print("8. Back")

            employee_management_choice = input("Enter your choice: ")

            if employee_management_choice == "1":
                person_id = input("Enter the person id: ")
                person_id = int(person_id)

                name = input("Enter the name of employee: ")

                if not Validator.validate_name(name):
                    print("Invalid name.")
                    continue

                phone = input("Enter the phone of employee: ")

                if not Validator.validate_phone(phone):
                    print("Invalid phone.")
                    continue

                email = input("Enter the email of employee: ")

                if not Validator.validate_email(email):
                    print("Invalid email.")
                    continue

                postcode = input("Enter the postcode of employee: ")

                employee_id = bank.generate_employee_id()

                designation = input("Enter the designation of employee: ")

                salary = input("Enter the salary of employee: ")
                salary = int(salary)

                if not Validator.validate_amount(salary):
                    print("Invalid salary.")
                    continue

                date_joined = date.today()

                employee = Employee(
                    person_id,
                    name,
                    phone,
                    email,
                    postcode,
                    employee_id,
                    designation,
                    salary,
                    date_joined
                )

                bank.add_employee(employee)

            elif employee_management_choice == "2":
                employee_id = input("Enter employee id: ")
                employee_id = int(employee_id)

                employee = bank.search_employee(employee_id)

                if employee:
                    new_designation = input(
                        "Enter new designation: "
                    ).strip()

                    if new_designation.lower() == "bank manager":

                        for emp in bank.employees:
                            if emp.designation == "Bank Manager":
                                print("Bank Manager already exists.")
                                break

                        else:
                            employee.update_designation("Bank Manager")
                            bank_manager = employee
                            print("Employee is now the Bank Manager.")

                    else:
                        employee.update_designation(new_designation)

                else:
                    print("Employee doesn't exist.")

            elif employee_management_choice == "3":
                employee_id = input("Enter employee id: ")
                employee_id = int(employee_id)

                employee = bank.search_employee(employee_id)

                if employee:
                    new_salary = input("Enter new salary: ")
                    new_salary = int(new_salary)

                    if not Validator.validate_amount(new_salary):
                        print("Invalid salary.")
                        continue

                    employee.update_salary(new_salary)

                else:
                    print("Employee doesn't exist.")

            elif employee_management_choice == "4":
                employee_id = input("Enter employee id: ")
                employee_id = int(employee_id)

                employee = bank.search_employee(employee_id)

                if employee:
                    new_status = input("Enter new status: ")
                    employee.update_status(new_status)

                else:
                    print("Employee doesn't exist.")

            elif employee_management_choice == "5":
                employee_id = input("Enter employee id: ")
                employee_id = int(employee_id)

                employee = bank.search_employee(employee_id)

                if employee:
                    employee.display()

                else:
                    print("Employee doesn't exist.")

            elif employee_management_choice == "6":
                bank.display_employees()

            elif employee_management_choice == "7":
                employee_id = input("Enter employee id: ")
                employee_id = int(employee_id)

                employee = bank.search_employee(employee_id)

                if employee:
                    bank.remove_employee(employee_id)

                    if employee == bank_manager:
                        bank_manager = None

                else:
                    print("Employee doesn't exist.")

            elif employee_management_choice == "8":
                pass

        if choice == "10":

            if bank_manager is None:
                print("No Bank Manager exists.")
                continue

            while True:
                print("\n========== BANK MANAGER MENU ==========")
                print("1. Add Employee")
                print("2. Remove Employee")
                print("3. View All Employees")
                print("4. View All Customers")
                print("5. View All Accounts")
                print("6. View Bank Report")
                print("7. Back to Main Menu")

                bank_management_choice = input("Enter your choice: ")

                if bank_management_choice == "1":

                    person_id = input("Enter the person id: ")
                    person_id = int(person_id)

                    name = input("Enter the name of employee: ")

                    if not Validator.validate_name(name):
                        print("Invalid name.")
                        continue

                    phone = input("Enter the phone of employee: ")

                    if not Validator.validate_phone(phone):
                        print("Invalid phone.")
                        continue

                    email = input("Enter the email of employee: ")

                    if not Validator.validate_email(email):
                        print("Invalid email.")
                        continue

                    postcode = input("Enter the postcode of employee: ")

                    employee_id = bank.generate_employee_id()

                    designation = input("Enter the designation of employee: ")

                    salary = input("Enter the salary of employee: ")
                    salary = int(salary)

                    if not Validator.validate_amount(salary):
                        print("Invalid salary.")
                        continue

                    date_joined = date.today()

                    employee = Employee(
                        person_id,
                        name,
                        phone,
                        email,
                        postcode,
                        employee_id,
                        designation,
                        salary,
                        date_joined
                    )

                    bank_manager.add_employee(bank, employee)

                elif bank_management_choice == "2":

                    employee_id = input("Enter employee id: ")
                    employee_id = int(employee_id)

                    employee = bank.search_employee(employee_id)

                    if employee:
                        bank_manager.remove_employee(
                            bank,
                            employee_id
                        )
                    else:
                        print("Employee doesn't exist.")

                elif bank_management_choice == "3":
                    bank_manager.view_all_employees(bank)

                elif bank_management_choice == "4":
                    bank_manager.view_all_customers(bank)

                elif bank_management_choice == "5":
                    bank_manager.view_all_accounts(bank)

                elif bank_management_choice == "6":
                    bank_manager.view_bank_report(bank)

                elif bank_management_choice == "7":
                    break

                else:
                    print("Invalid choice.")

        if choice == "11":
            break


if __name__ == "__main__":
    main()