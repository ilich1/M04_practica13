class User:
    def _init_(self, name, age, email, address, phone_number, occupation):
        self.name = name
        self.age = age
        self.email = email
        self.address = address
        self.phone_number = phone_number
        self.occupation = occupation

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_occupation(self):
        return self.occupation

    def set_occupation(self, occupation):
        self.occupation = occupation

    def salutacio(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Email: ", self.email)
        print("Address: ", self.address)
        print("Phone Number: ", self.phone_number)
        print("Occupation: ", self.occupation)