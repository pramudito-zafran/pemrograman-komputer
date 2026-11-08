class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login = 0

    def describe_user(self):
        print(f'First name = {self.first_name}')
        print(f'Last name = {self.last_name}')
        print(f'Age = {self.age}')

    def greets_user(self):
        print(f'Hello {self.first_name} {self.last_name}')

    def increment_login (self):
        self.login += 1

    def reset_login (self):
        self.login = 0

class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(f"Admin's privileges for {self.first_name.title()} {self.last_name.title()}:")
        for privilege in self.privileges:
            print(f'- {privilege.capitalize()}')

Administrator = Admin('Bryan', 'Obang', 20)
Administrator.show_privileges()