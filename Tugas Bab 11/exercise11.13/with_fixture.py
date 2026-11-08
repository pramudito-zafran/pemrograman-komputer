import pytest
from pegawai import Employee

@pytest.fixture
def sample_employee():
    """A fixture providing a standard Employee instance for tests."""
    return Employee('Jane', 'Doe', 60000)

def test_give_default_raise(sample_employee):
    """Test that a default raise of $5,000 is applied correctly using a fixture."""
    sample_employee.give_raise()
    assert sample_employee.annual_salary == 65000

def test_give_custom_raise(sample_employee):
    """Test that a custom raise amount is applied correctly using a fixture."""
    sample_employee.give_raise(10000)
    assert sample_employee.annual_salary == 70000
