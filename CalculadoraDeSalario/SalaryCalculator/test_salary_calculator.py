from ..Employee.employee import Employee
from .salaryCalculator import SalaryCalculator


def test_exist_salary_calculator():
    salaryCalculator = SalaryCalculator()

    assert salaryCalculator != None


def test_exist_calculate():
    employee = Employee()

    salaryCalculator = SalaryCalculator()
    salaryCalculator.calculate(employee)


def test_calculate_return():
    employee = Employee()

    salaryCalculator = SalaryCalculator()

    assert salaryCalculator.calculate(employee) == 0
