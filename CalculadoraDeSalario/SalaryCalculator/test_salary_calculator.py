from ..Employee.employee import Employee
from .salaryCalculator import SalaryCalculator

salaryCalculator = SalaryCalculator()


def test_exist_salary_calculator():
    assert salaryCalculator != None


def test_exist_calculate():
    employee = Employee()

    salaryCalculator.calculate(employee)


def test_calculate_return():
    employee = Employee()

    assert salaryCalculator.calculate(employee) == 0
