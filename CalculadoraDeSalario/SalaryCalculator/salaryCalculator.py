from ..Employee.employee import Employee


class SalaryCalculator:
    def calculate(self, employee: Employee) -> float:
        discount_value = 0.2

        salary_threshold = 3000

        employee_base_salary = employee.base_salary

        if employee_base_salary < salary_threshold:
            discount_value = 0.1

        liquid_salary = employee_base_salary * (1 - discount_value)

        return liquid_salary
