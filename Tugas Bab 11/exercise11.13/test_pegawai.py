from pegawai import Employee

def test_give_default_raise():
    """Test that a default raise of $5,000 is applied correctly."""
    employee = Employee('Jane', 'Doe', 60000)
    employee.give_raise()
    assert employee.annual_salary == 65000

def test_give_custom_raise():
    """Test that a custom raise amount is applied correctly."""
    employee = Employee('Jane', 'Doe', 60000)
    employee.give_raise(10000)
    assert employee.annual_salary == 70000
