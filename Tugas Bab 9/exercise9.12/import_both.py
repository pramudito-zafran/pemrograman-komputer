from admin_privileges import Admin

Administrator = Admin('Bryan', 'Obang', 20)
Administrator.describe_user()
print('-'*20)
Administrator.privileges.show_privileges()
