class Person:
    def __init__(self, person_id, name, phone, email, post_code):
        self.person_id = person_id
        self.name = name
        self.phone = phone
        self.email = email
        self.post_code = post_code
    def display_info(self):
        print(f"Name : {self.name}")
        print(f"ID : {self.person_id}")
        print(f"Phone : {self.phone}")
        print(f"Email : {self.email}")
        print(f"Post Code : {self.post_code}")
    def update_name(self, newName):
        self.name = newName
    def update_phone(self, new_Phone):
        self.phone = new_Phone
    def update_email(self, new_Email):
        self.email = new_Email
    def to_dict(self):
        return {
            "person_id" : self.person_id,
            "name" : self.name,
            "phone" : self.phone,
            "email" : self.email,
            "post_code" : self.post_code
        }
    @classmethod
    def from_dict(cls, data):
        return cls(**data)