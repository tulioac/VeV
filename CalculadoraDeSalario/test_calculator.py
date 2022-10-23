from .salaryCalculator import SalaryCalculator


def test_exist_salary_calculator():
    salaryCalculator = SalaryCalculator()

    assert salaryCalculator != None


def test_exist_employee():
    employee = Employee()

    assert employee != None
