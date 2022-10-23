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


def test_calculate_developer_salary_over_3000():
    base_salary = 5_000

    employee = Employee(role="Developer", base_salary=base_salary)

    developer_liquid_salary = base_salary * 0.8

    assert developer_liquid_salary == salaryCalculator.calculate(employee)


def test_calculate_developer_salary_equals_3000():
    base_salary = 3_000

    employee = Employee(role="Developer", base_salary=base_salary)

    developer_liquid_salary = base_salary * 0.8

    assert developer_liquid_salary == salaryCalculator.calculate(employee)
