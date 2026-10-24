class Validator:
    @staticmethod
    def validate_name(name):
        if not isinstance(name, str):
            return False
        name = name.strip()
        if name == "":
            return False
        if not name.replace(" ", "").isalpha():
            return False
        return True
    @staticmethod
    def validate_phone(phone):
        if not isinstance(phone, str):
            return False
        phone = phone.strip()
        if phone == "":
            return False
        if not phone.isdigit():
            return False
        if len(phone) != 11:
            return False
        if not phone.startswith('03'):
            return False
        return True
    @staticmethod
    def validate_email(email):
        if not isinstance(email, str):
            return False
        email = email.strip()
        if email == "":
            return False
        if email.count("@") != 1:
            return False
        username, domain = email.split("@")
        if username == "":
            return False
        if domain == "":
            return False
        if domain.startswith("."):
            return False
        if domain.endswith("."):
            return False
        if domain.count(".") < 1 or domain.count(".") > 3:
            return False
        return True
    @staticmethod
    def validate_amount(amount):
        if not isinstance(amount, (float, int)):
            return False
        if not amount > 0:
            return False
        return True
    @staticmethod
    def validate_account_number(account_number):
        if not isinstance(account_number, int):
            return False
        if not account_number>0:
            return False
        if len(str(account_number))<6:
            return False
        return True
    @staticmethod
    def validate_pin(pin):
        if not isinstance(pin, str):
            return False
        pin = pin.strip()
        if pin == "":
            return False
        if not pin.isdigit():
            return False
        if len(pin) != 4:
            return False
        return True