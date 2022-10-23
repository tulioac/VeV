from ..Employee.employee import Employee


class SalaryCalculator:
    def calculate(self, employee: Employee) -> float:
        return employee.base_salary * 0.8
