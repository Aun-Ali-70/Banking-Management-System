from person import Person
from datetime import date
class Employee(Person):
    def __init__(self, person_id, name, phone, email, post_code, employee_id, designation, salary, date_joined, status = "Active"):
        super().__init__(person_id, name, phone, email, post_code)
        self.employee_id = employee_id
        self.designation = designation
        self.salary = salary
        self.date_joined = date_joined
        self.status = status
    def display(self):
        self.display_info()
        print(f"Employee ID : {self.employee_id}")
        print(f"Employee Designation : {self.designation}")
        print(f"Employee Salary : {self.salary}")
        print(f"Date of Joined : {self.date_joined}")
        print(f"Employment status : {self.status}\n\n")
    def update_designation(self, new_designation):
        self.designation = new_designation
    def update_salary(self, new_salary):
        if new_salary<0:
            print("Salary can not be negative.")
            return False
        self.salary = new_salary
        return True
    def update_status(self, new_status):
        self.status = new_status
    def to_dict(self):
        data = super().to_dict()
        data["employee_id"] = self.employee_id
        data["designation"] = self.designation
        data["salary"] = self.salary
        data["date_joined"] = self.date_joined.isoformat()
        data["status"] = self.status
        return data
    @classmethod
    def from_dict(cls, data):
        data = data.copy()
        data["date_joined"] = date.fromisoformat(data["date_joined"])
        return cls(**data)