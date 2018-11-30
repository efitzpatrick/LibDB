class User():
    def __init__(self, id, email):
        self.id = id
        self.email = email

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email
