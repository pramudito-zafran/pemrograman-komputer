class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f'First name = {self.first_name}')
        print(f'Last name = {self.last_name}')
        print(f'Age = {self.age}')

    def greets_user(self):
        print(f'Hello {self.first_name} {self.last_name}')

User1 = User ('Aan', 'Suraan', 20)
User2 = User ('Febian', 'Putra', 20)
User3 = User ('Mamang', 'Suramang', 10)

User1.describe_user()
User1.greets_user()

print('-'*50)
User2.describe_user()
User2.greets_user()

print('-'*50)
User3.describe_user()
User3.greets_user()


