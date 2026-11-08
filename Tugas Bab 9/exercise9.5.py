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

User1 = User ('Aan', 'Suraan', 20)

print("===Incrementing login attempts===")
User1.increment_login()
User1.increment_login()
User1.increment_login()

print(f"Current login attempts: {User1.login}")

print("\n===Resetting login attempts===")
User1.reset_login()

print(f"Current login attempts: {User1.login}")
