class User():
    def __init__(self, id, email, privilege):
        self.id = id
        self.email = email
        if privilege == 'admin':
            self.privilege = True
        else:
            self.privilege = False

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_privilege(self):
        return self.privilege

    def set_privilege(self, privilege):
        self.privilege = privilege
