from ..Employee.employee import Employee
from .salaryCalculator import SalaryCalculator


def test_exist_salary_calculator():
    salaryCalculator = SalaryCalculator()

    assert salaryCalculator != None


def test_exist_calculate():
    employee = Employee()

    salaryCalculator = SalaryCalculator()
    salaryCalculator.calculate(employee)
